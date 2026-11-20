package com.horsecoder.common.whuTalent.core.agent;

import org.springframework.stereotype.Service;

import javax.annotation.PreDestroy;
import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.HashSet;
import java.util.LinkedHashMap;
import java.util.LinkedHashSet;
import java.util.List;
import java.util.Map;
import java.util.Set;
import java.util.UUID;
import java.util.concurrent.Callable;
import java.util.concurrent.ExecutionException;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.Future;
import java.util.concurrent.TimeUnit;
import java.util.concurrent.TimeoutException;
import java.util.regex.Pattern;

/** Validates and runs a bounded DAG of registered atomic agents, fan-out layers execute concurrently. */
@Service
public class AgentOrganizationCoordinator {
    private static final int MAX_NODES = 16;
    private static final int MAX_PARALLEL_AGENTS = 4;
    private static final long MAX_ORGANIZATION_MILLIS = 60000L;
    private static final long MAX_NODE_MILLIS = 15000L;
    private static final Pattern SAFE_NODE_ID = Pattern.compile("[A-Za-z0-9_-]{1,64}");
    private final Map<String, Agent> agents;
    private final ExecutorService executor = Executors.newFixedThreadPool(MAX_PARALLEL_AGENTS);

    public AgentOrganizationCoordinator(List<Agent> availableAgents) {
        Map<String, Agent> indexed = new LinkedHashMap<String, Agent>();
        if (availableAgents != null) {
            for (Agent agent : availableAgents) {
                if (agent == null || isBlank(agent.getAgentId())) continue;
                if (indexed.put(agent.getAgentId(), agent) != null) {
                    throw new IllegalStateException("Duplicate Agent ID: " + agent.getAgentId());
                }
            }
        }
        this.agents = Collections.unmodifiableMap(indexed);
    }

    public List<AgentDescriptor> listAgents() {
        List<AgentDescriptor> descriptors = new ArrayList<AgentDescriptor>();
        for (Agent agent : agents.values()) descriptors.add(agent.getDescriptor());
        return Collections.unmodifiableList(descriptors);
    }

    public AgentResult execute(AgentOrganizationTask organizationTask) {
        String requestId = organizationTask == null || isBlank(organizationTask.getRequestId())
                ? UUID.randomUUID().toString() : organizationTask.getRequestId();
        long startedAt = System.currentTimeMillis();
        try {
            List<AgentOrganizationTask.Node> nodes = validateAndCopy(organizationTask);
            List<List<AgentOrganizationTask.Node>> layers = buildLayers(nodes);
            if (layers.size() > 8) throw new IllegalArgumentException("organization exceeds maximum depth of 8");
            String organizationType = classify(nodes);
            Map<String, AgentResult> completed = new LinkedHashMap<String, AgentResult>();

            for (List<AgentOrganizationTask.Node> layer : layers) {
                List<Future<NodeResult>> futures = new ArrayList<Future<NodeResult>>();
                List<AgentOrganizationTask.Node> submitted = new ArrayList<AgentOrganizationTask.Node>();
                for (AgentOrganizationTask.Node node : layer) {
                    if (hasFailedDependency(node, completed)) {
                        AgentResult skipped = AgentResult.failure(requestId, node.getAgentId(),
                                "UPSTREAM_FAILED", "Agent was skipped because a dependency did not succeed");
                        skipped.setOrganizationNodeId(node.getNodeId());
                        completed.put(node.getNodeId(), skipped);
                        continue;
                    }
                    Agent agent = agents.get(node.getAgentId());
                    AgentTask childTask = createChildTask(requestId, organizationTask, node, completed);
                    futures.add(executor.submit(new AgentCall(agent, childTask, node.getNodeId(), requestId)));
                    submitted.add(node);
                }
                for (int index = 0; index < futures.size(); index++) {
                    try {
                        long remaining = MAX_ORGANIZATION_MILLIS - (System.currentTimeMillis() - startedAt);
                        if (remaining <= 0) throw new TimeoutException("organization timeout");
                        NodeResult nodeResult = futures.get(index).get(Math.min(remaining, MAX_NODE_MILLIS), TimeUnit.MILLISECONDS);
                        completed.put(nodeResult.nodeId, nodeResult.result);
                        if (!"SUCCEEDED".equals(nodeResult.result.getStatus())) {
                            cancelSiblings(futures, index);
                            for (int pending = index + 1; pending < submitted.size(); pending++) {
                                AgentOrganizationTask.Node sibling = submitted.get(pending);
                                AgentResult cancelled = AgentResult.failure(requestId, sibling.getAgentId(), "SIBLING_CANCELLED", "Cancelled after a peer in the same layer failed");
                                cancelled.setOrganizationNodeId(sibling.getNodeId());
                                completed.put(sibling.getNodeId(), cancelled);
                            }
                            break;
                        }
                    } catch (TimeoutException exception) {
                        cancelSiblings(futures, index);
                        AgentOrganizationTask.Node node = submitted.get(index);
                        AgentResult failed = AgentResult.failure(requestId, node.getAgentId(),
                                "AGENT_TIMEOUT", "Agent node exceeded its execution timeout");
                        failed.setOrganizationNodeId(node.getNodeId());
                        completed.put(node.getNodeId(), failed);
                        for (int pending = index + 1; pending < submitted.size(); pending++) {
                            AgentOrganizationTask.Node sibling = submitted.get(pending);
                            AgentResult cancelled = AgentResult.failure(requestId, sibling.getAgentId(), "SIBLING_CANCELLED", "Cancelled after a peer in the same layer timed out");
                            cancelled.setOrganizationNodeId(sibling.getNodeId());
                            completed.put(sibling.getNodeId(), cancelled);
                        }
                        break;
                    } catch (InterruptedException exception) {
                        Thread.currentThread().interrupt();
                        AgentOrganizationTask.Node node = submitted.get(index);
                        AgentResult failed = AgentResult.failure(requestId, node.getAgentId(),
                                "ORGANIZATION_INTERRUPTED", "Agent organization execution was interrupted");
                        failed.setOrganizationNodeId(node.getNodeId());
                        completed.put(node.getNodeId(), failed);
                    } catch (ExecutionException exception) {
                        AgentOrganizationTask.Node node = submitted.get(index);
                        AgentResult failed = AgentResult.failure(requestId, node.getAgentId(),
                                "AGENT_EXECUTION_FAILED", safeMessage(exception.getCause()));
                        failed.setOrganizationNodeId(node.getNodeId());
                        completed.put(node.getNodeId(), failed);
                    }
                }
            }
            return aggregate(requestId, organizationType, nodes, completed, startedAt);
        } catch (IllegalArgumentException exception) {
            AgentResult result = AgentResult.failure(requestId, "agent-organization-coordinator",
                    "INVALID_ORGANIZATION", exception.getMessage());
            result.setElapsedMs(System.currentTimeMillis() - startedAt);
            return result;
        } catch (Exception exception) {
            AgentResult result = AgentResult.failure(requestId, "agent-organization-coordinator",
                    "ORGANIZATION_FAILED", safeMessage(exception));
            result.setElapsedMs(System.currentTimeMillis() - startedAt);
            return result;
        }
    }

    private static void cancelSiblings(List<Future<NodeResult>> futures, int finishedIndex) {
        for (int index = 0; index < futures.size(); index++) {
            if (!futures.get(index).isDone()) futures.get(index).cancel(true);
        }
    }

    @PreDestroy
    public void shutdown() { executor.shutdown(); }

    private List<AgentOrganizationTask.Node> validateAndCopy(AgentOrganizationTask task) {
        if (task == null) throw new IllegalArgumentException("organization task is required");
        if (task.getNodes() == null || task.getNodes().isEmpty()) {
            throw new IllegalArgumentException("organization must contain at least one node");
        }
        if (task.getNodes().size() > MAX_NODES) throw new IllegalArgumentException("organization exceeds 16 nodes");

        List<AgentOrganizationTask.Node> nodes = new ArrayList<AgentOrganizationTask.Node>();
        Map<String, AgentOrganizationTask.Node> byId = new LinkedHashMap<String, AgentOrganizationTask.Node>();
        for (AgentOrganizationTask.Node source : task.getNodes()) {
            if (source == null || isBlank(source.getNodeId()) || !SAFE_NODE_ID.matcher(source.getNodeId()).matches()) {
                throw new IllegalArgumentException("each node requires a safe nodeId of 1 to 64 letters, digits, '_' or '-'");
            }
            if (byId.containsKey(source.getNodeId())) throw new IllegalArgumentException("duplicate nodeId: " + source.getNodeId());
            if (isBlank(source.getAgentId()) || !agents.containsKey(source.getAgentId())) {
                throw new IllegalArgumentException("unknown agentId for node " + source.getNodeId());
            }
            String question = isBlank(source.getQuestion()) ? task.getQuestion() : source.getQuestion();
            if (isBlank(question)) throw new IllegalArgumentException("question is required for node " + source.getNodeId());
            if (question.length() > 2000) throw new IllegalArgumentException("question exceeds 2000 characters for node " + source.getNodeId());
            AgentOrganizationTask.Node copy = new AgentOrganizationTask.Node();
            copy.setNodeId(source.getNodeId());
            copy.setAgentId(source.getAgentId());
            copy.setQuestion(question);
            List<String> dependencies = source.getDependsOn() == null
                    ? new ArrayList<String>() : new ArrayList<String>(source.getDependsOn());
            if (dependencies.size() > MAX_NODES) throw new IllegalArgumentException("too many dependencies for node " + source.getNodeId());
            if (new HashSet<String>(dependencies).size() != dependencies.size()) {
                throw new IllegalArgumentException("duplicate dependency for node " + source.getNodeId());
            }
            copy.setDependsOn(dependencies);
            nodes.add(copy);
            byId.put(copy.getNodeId(), copy);
        }
        for (AgentOrganizationTask.Node node : nodes) {
            for (String dependency : node.getDependsOn()) {
                if (!byId.containsKey(dependency)) throw new IllegalArgumentException("unknown dependency " + dependency + " for node " + node.getNodeId());
                if (node.getNodeId().equals(dependency)) throw new IllegalArgumentException("node cannot depend on itself: " + node.getNodeId());
            }
        }
        return nodes;
    }

    private static List<List<AgentOrganizationTask.Node>> buildLayers(List<AgentOrganizationTask.Node> nodes) {
        Set<String> completed = new LinkedHashSet<String>();
        Set<String> remaining = new LinkedHashSet<String>();
        for (AgentOrganizationTask.Node node : nodes) remaining.add(node.getNodeId());
        List<List<AgentOrganizationTask.Node>> layers = new ArrayList<List<AgentOrganizationTask.Node>>();
        Map<String, AgentOrganizationTask.Node> byId = new HashMap<String, AgentOrganizationTask.Node>();
        for (AgentOrganizationTask.Node node : nodes) byId.put(node.getNodeId(), node);
        while (!remaining.isEmpty()) {
            List<AgentOrganizationTask.Node> ready = new ArrayList<AgentOrganizationTask.Node>();
            for (String nodeId : remaining) {
                AgentOrganizationTask.Node node = byId.get(nodeId);
                if (completed.containsAll(node.getDependsOn())) ready.add(node);
            }
            if (ready.isEmpty()) throw new IllegalArgumentException("organization graph contains a cycle");
            layers.add(ready);
            for (AgentOrganizationTask.Node node : ready) {
                completed.add(node.getNodeId());
                remaining.remove(node.getNodeId());
            }
        }
        return layers;
    }

    private static AgentTask createChildTask(String requestId,
                                              AgentOrganizationTask parent,
                                              AgentOrganizationTask.Node node,
                                              Map<String, AgentResult> completed) {
        AgentTask child = new AgentTask();
        child.setRequestId(requestId);
        child.setQuestion(node.getQuestion());
        Map<String, Object> context = copyMap(parent.getContext());
        context.put("organizationNodeId", node.getNodeId());
        List<AgentResult> upstream = new ArrayList<AgentResult>();
        for (String dependency : node.getDependsOn()) upstream.add(completed.get(dependency));
        context.put("upstreamResults", upstream);
        child.setContext(context);
        child.setConstraints(copyMap(parent.getConstraints()));
        return child;
    }

    private static boolean hasFailedDependency(AgentOrganizationTask.Node node, Map<String, AgentResult> completed) {
        for (String dependency : node.getDependsOn()) {
            AgentResult result = completed.get(dependency);
            if (result == null || !"SUCCEEDED".equals(result.getStatus())) return true;
        }
        return false;
    }

    private static AgentResult aggregate(String requestId, String organizationType,
                                         List<AgentOrganizationTask.Node> nodes,
                                         Map<String, AgentResult> completed, long startedAt) {
        AgentResult result = new AgentResult();
        result.setRequestId(requestId);
        result.setAgentId("agent-organization-coordinator");
        result.setOrganizationType(organizationType);
        List<AgentResult> orderedResults = new ArrayList<AgentResult>();
        List<AgentResult> successfulLeaves = new ArrayList<AgentResult>();
        int successes = 0;
        boolean hasClarification = false;
        for (AgentOrganizationTask.Node node : nodes) {
            AgentResult child = completed.get(node.getNodeId());
            if (child == null) {
                child = AgentResult.failure(requestId, node.getAgentId(), "AGENT_NOT_RUN", "Agent node did not run");
                child.setOrganizationNodeId(node.getNodeId());
            }
            orderedResults.add(child);
            if ("SUCCEEDED".equals(child.getStatus())) successes++;
            if ("NEEDS_CLARIFICATION".equals(child.getStatus())) hasClarification = true;
            if (isLeaf(node, nodes) && "SUCCEEDED".equals(child.getStatus())) successfulLeaves.add(child);
        }
        result.setSubResults(orderedResults);
        if (successes == nodes.size()) result.setStatus("SUCCEEDED");
        else if (successes > 0) result.setStatus("PARTIAL");
        else result.setStatus(hasClarification ? "NEEDS_CLARIFICATION" : "FAILED");
        result.setElapsedMs(System.currentTimeMillis() - startedAt);
        result.setAnswer("Agent organization " + organizationType + " completed: " + successes + "/" + nodes.size() + " node(s) succeeded.");

        if (!successfulLeaves.isEmpty()) {
            // Deterministic merge policy: highest confidence; ties preserve request node order.
            AgentResult leaf = successfulLeaves.get(0);
            for (AgentResult candidate : successfulLeaves) if (candidate.getConfidence() > leaf.getConfidence()) leaf = candidate;
            result.setSql(leaf.getSql());
            result.setParameters(leaf.getParameters());
            result.setRows(leaf.getRows());
            result.setHitCount(leaf.getHitCount());
            result.setLimitTruncated(leaf.isLimitTruncated());
            if (successfulLeaves.size() > 1) result.setAnswer(result.getAnswer() + " Selected the highest-confidence successful terminal candidate (ties preserve request order).");
        } else if (successfulLeaves.isEmpty() && hasClarification) {
            for (AgentResult child : orderedResults) {
                if ("NEEDS_CLARIFICATION".equals(child.getStatus())) {
                    result.setAnswer(child.getAnswer());
                    break;
                }
            }
        }
        if ("FAILED".equals(result.getStatus())) {
            result.setErrorCode("ORGANIZATION_NODE_FAILED");
            result.setErrorMessage("No terminal Agent completed successfully; inspect subResults for node errors");
        }
        return result;
    }

    private static boolean isLeaf(AgentOrganizationTask.Node candidate, List<AgentOrganizationTask.Node> nodes) {
        for (AgentOrganizationTask.Node node : nodes) if (node.getDependsOn().contains(candidate.getNodeId())) return false;
        return true;
    }

    private static String classify(List<AgentOrganizationTask.Node> nodes) {
        Map<String, Integer> outDegree = new HashMap<String, Integer>();
        int roots = 0;
        int leaves = 0;
        for (AgentOrganizationTask.Node node : nodes) {
            if (node.getDependsOn().isEmpty()) roots++;
            outDegree.put(node.getNodeId(), 0);
        }
        for (AgentOrganizationTask.Node node : nodes) {
            for (String dependency : node.getDependsOn()) outDegree.put(dependency, outDegree.get(dependency) + 1);
        }
        for (Integer degree : outDegree.values()) if (degree == 0) leaves++;
        int edges = 0;
        boolean branchingOrMerge = false;
        Map<String, Integer> inDegree = new HashMap<String, Integer>();
        for (AgentOrganizationTask.Node node : nodes) {
            inDegree.put(node.getNodeId(), node.getDependsOn().size());
            edges += node.getDependsOn().size();
        }
        for (Integer degree : outDegree.values()) if (degree > 1) branchingOrMerge = true;
        for (Integer degree : inDegree.values()) if (degree > 1) branchingOrMerge = true;
        if (roots == 1 && leaves == 1 && edges == nodes.size() - 1 && !branchingOrMerge) return "ONE_TO_ONE";
        if (roots == 1 && leaves > 1) return "ONE_TO_MANY";
        if (roots > 1 && leaves > 1) return "MANY_TO_MANY";
        return "CUSTOM_DAG";
    }

    private static Map<String, Object> copyMap(Map<String, Object> source) {
        return source == null ? new LinkedHashMap<String, Object>() : new LinkedHashMap<String, Object>(source);
    }

    private static String safeMessage(Throwable exception) {
        if (exception == null || isBlank(exception.getMessage())) return "The Agent node failed";
        String message = exception.getMessage();
        return message.length() > 300 ? message.substring(0, 300) : message;
    }

    private static boolean isBlank(String value) { return value == null || value.trim().isEmpty(); }

    private static final class AgentCall implements Callable<NodeResult> {
        private final Agent agent;
        private final AgentTask task;
        private final String nodeId;
        private final String requestId;

        private AgentCall(Agent agent, AgentTask task, String nodeId, String requestId) {
            this.agent = agent;
            this.task = task;
            this.nodeId = nodeId;
            this.requestId = requestId;
        }

        @Override
        public NodeResult call() {
            try {
                AgentResult result = agent.execute(task);
                if (result == null) result = AgentResult.failure(requestId, agent.getAgentId(), "EMPTY_AGENT_RESULT", "Agent returned no result");
                result.setOrganizationNodeId(nodeId);
                if (isBlank(result.getRequestId())) result.setRequestId(requestId);
                if (isBlank(result.getAgentId())) result.setAgentId(agent.getAgentId());
                return new NodeResult(nodeId, result);
            } catch (Exception exception) {
                AgentResult failed = AgentResult.failure(requestId, agent.getAgentId(), "AGENT_EXECUTION_FAILED", safeMessage(exception));
                failed.setOrganizationNodeId(nodeId);
                return new NodeResult(nodeId, failed);
            }
        }
    }

    private static final class NodeResult {
        private final String nodeId;
        private final AgentResult result;
        private NodeResult(String nodeId, AgentResult result) { this.nodeId = nodeId; this.result = result; }
    }
}
