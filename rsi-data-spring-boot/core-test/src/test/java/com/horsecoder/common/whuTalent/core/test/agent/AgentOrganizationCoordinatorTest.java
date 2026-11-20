package com.horsecoder.common.whuTalent.core.test.agent;

import com.horsecoder.common.whuTalent.core.agent.Agent;
import com.horsecoder.common.whuTalent.core.agent.AgentDescriptor;
import com.horsecoder.common.whuTalent.core.agent.AgentOrganizationCoordinator;
import com.horsecoder.common.whuTalent.core.agent.AgentOrganizationTask;
import com.horsecoder.common.whuTalent.core.agent.AgentResult;
import com.horsecoder.common.whuTalent.core.agent.AgentTask;
import com.horsecoder.common.whuTalent.core.agent.single.SqlValidatorAgent;
import org.junit.After;
import org.junit.Assert;
import org.junit.Test;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;
import java.util.Map;

public class AgentOrganizationCoordinatorTest {
    private final RecordingAgent alpha = new RecordingAgent("alpha");
    private final RecordingAgent beta = new RecordingAgent("beta");
    private final RecordingAgent gamma = new RecordingAgent("gamma");
    private final AgentOrganizationCoordinator coordinator = new AgentOrganizationCoordinator(Arrays.<Agent>asList(alpha, beta, gamma));

    @After
    public void shutDownCoordinator() { coordinator.shutdown(); }

    @Test
    public void executesOneToOnePipelineAndPassesUpstreamEvidence() {
        AgentOrganizationTask task = task(node("plan", "alpha"), node("query", "beta", "plan"));

        AgentResult result = coordinator.execute(task);

        Assert.assertEquals("SUCCEEDED", result.getStatus());
        Assert.assertEquals("ONE_TO_ONE", result.getOrganizationType());
        Assert.assertEquals(2, result.getSubResults().size());
        Assert.assertEquals("SELECT 'beta'", result.getSql());
        Assert.assertEquals(1, beta.lastTask.getContext().get("upstreamResults") instanceof List
                ? ((List<?>) beta.lastTask.getContext().get("upstreamResults")).size() : -1);
    }

    @Test
    public void executesOneToManyFanOutAndSelectsFirstSuccessfulTerminal() {
        AgentOrganizationTask task = task(node("root", "alpha"), node("left", "beta", "root"), node("right", "gamma", "root"));

        AgentResult result = coordinator.execute(task);

        Assert.assertEquals("SUCCEEDED", result.getStatus());
        Assert.assertEquals("ONE_TO_MANY", result.getOrganizationType());
        Assert.assertEquals("SELECT 'beta'", result.getSql());
        Assert.assertEquals(3, result.getSubResults().size());
        Assert.assertTrue(result.getAnswer().contains("highest-confidence"));
    }

    @Test
    public void executesManyToManyMergeWithAllParentResults() {
        AgentOrganizationTask task = task(node("source-a", "alpha"), node("source-b", "beta"),
                node("merge-a", "gamma", "source-a", "source-b"), node("merge-b", "alpha", "source-a", "source-b"));

        AgentResult result = coordinator.execute(task);

        Assert.assertEquals("SUCCEEDED", result.getStatus());
        Assert.assertEquals("MANY_TO_MANY", result.getOrganizationType());
        Assert.assertEquals(2, ((List<?>) gamma.lastTask.getContext().get("upstreamResults")).size());
    }

    @Test
    public void classifiesSingleRootDiamondAsCustomDagAndPromotesOneCandidate() {
        AgentOrganizationTask task = task(node("root", "alpha"), node("left", "beta", "root"),
                node("right", "gamma", "root"), node("merge", "alpha", "left", "right"));
        AgentResult result = coordinator.execute(task);
        Assert.assertEquals("CUSTOM_DAG", result.getOrganizationType());
        Assert.assertNotNull("a deterministic terminal SQL candidate should be promoted", result.getSql());
    }

    @Test
    public void propagatesClarificationWithoutCallingDependentAgent() {
        alpha.clarify = true;
        AgentOrganizationTask task = task(node("source", "alpha"), node("dependent", "beta", "source"));
        AgentResult result = coordinator.execute(task);
        Assert.assertEquals("NEEDS_CLARIFICATION", result.getStatus());
        Assert.assertEquals("UPSTREAM_FAILED", result.getSubResults().get(1).getErrorCode());
        Assert.assertNull(beta.lastTask);
    }

    @Test
    public void reportsPartialWhenPriorLayerSucceededAndFollowingLayerFails() {
        beta.fail = true;
        AgentOrganizationTask task = task(node("seed", "alpha"), node("failed", "beta", "seed"));
        AgentResult result = coordinator.execute(task);
        Assert.assertEquals("PARTIAL", result.getStatus());
        Assert.assertEquals(1, result.getSubResults().stream().filter(item -> "SUCCEEDED".equals(item.getStatus())).count());
    }

    @Test
    public void validatorConsumesUpstreamSqlInsteadOfReplanningTheQuestion() {
        AgentOrganizationCoordinator validatingCoordinator = new AgentOrganizationCoordinator(Arrays.<Agent>asList(
                alpha, beta, new SqlValidatorAgent()));
        try {
            AgentOrganizationTask task = task(node("draft", "alpha"), node("validate", "sql-validator", "draft"));
            AgentResult result = validatingCoordinator.execute(task);
            Assert.assertEquals("SUCCEEDED", result.getStatus());
            Assert.assertEquals("SELECT 'alpha'", result.getSql());
        } finally {
            validatingCoordinator.shutdown();
        }
    }

    @Test
    public void timesOutAndCancelsSlowAgentNode() {
        alpha.sleepMillis = 20000;
        AgentResult result = coordinator.execute(task(node("slow", "alpha")));
        Assert.assertEquals("FAILED", result.getStatus());
        Assert.assertEquals("AGENT_TIMEOUT", result.getSubResults().get(0).getErrorCode());
    }

    @Test
    public void rejectsCyclesBeforeRunningAnyAgent() {
        AgentOrganizationTask task = task(node("a", "alpha", "b"), node("b", "beta", "a"));

        AgentResult result = coordinator.execute(task);

        Assert.assertEquals("FAILED", result.getStatus());
        Assert.assertEquals("INVALID_ORGANIZATION", result.getErrorCode());
        Assert.assertNull(alpha.lastTask);
        Assert.assertNull(beta.lastTask);
    }

    @Test
    public void stopsDependentNodeWhenUpstreamAgentFails() {
        alpha.fail = true;
        AgentOrganizationTask task = task(node("source", "alpha"), node("dependent", "beta", "source"));

        AgentResult result = coordinator.execute(task);

        Assert.assertEquals("FAILED", result.getStatus());
        Assert.assertEquals("UPSTREAM_FAILED", result.getSubResults().get(1).getErrorCode());
        Assert.assertNull(beta.lastTask);
    }

    private static AgentOrganizationTask task(AgentOrganizationTask.Node... nodes) {
        AgentOrganizationTask task = new AgentOrganizationTask();
        task.setRequestId("test-request");
        task.setQuestion("count the records");
        task.setNodes(Arrays.asList(nodes));
        return task;
    }

    private static AgentOrganizationTask.Node node(String nodeId, String agentId, String... dependencies) {
        AgentOrganizationTask.Node node = new AgentOrganizationTask.Node();
        node.setNodeId(nodeId);
        node.setAgentId(agentId);
        node.setDependsOn(Arrays.asList(dependencies));
        return node;
    }

    private static final class RecordingAgent implements Agent {
        private final String agentId;
        private AgentTask lastTask;
        private boolean fail;
        private boolean clarify;
        private long sleepMillis;

        private RecordingAgent(String agentId) { this.agentId = agentId; }
        @Override public String getAgentId() { return agentId; }
        @Override public AgentDescriptor getDescriptor() {
            return new AgentDescriptor(agentId, "TEST", Collections.singletonList("test"));
        }
        @Override public AgentResult execute(AgentTask task) {
            lastTask = task;
            if (sleepMillis > 0) {
                try { Thread.sleep(sleepMillis); }
                catch (InterruptedException exception) { Thread.currentThread().interrupt(); return AgentResult.failure(task.getRequestId(), agentId, "INTERRUPTED", "cancelled"); }
            }
            if (clarify) {
                AgentResult result = new AgentResult();
                result.setRequestId(task.getRequestId()); result.setAgentId(agentId);
                result.setStatus("NEEDS_CLARIFICATION"); result.setAnswer("please clarify");
                return result;
            }
            if (fail) return AgentResult.failure(task.getRequestId(), agentId, "TEST_FAILURE", "intentional test failure");
            AgentResult result = new AgentResult();
            result.setRequestId(task.getRequestId());
            result.setAgentId(agentId);
            result.setStatus("SUCCEEDED");
            result.setSql("SELECT '" + agentId + "'");
            result.setRows(new ArrayList<Map<String, Object>>());
            return result;
        }
    }
}
