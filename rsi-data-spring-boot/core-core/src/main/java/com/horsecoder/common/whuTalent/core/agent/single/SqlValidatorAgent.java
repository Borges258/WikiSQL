package com.horsecoder.common.whuTalent.core.agent.single;

import com.horsecoder.common.whuTalent.core.agent.Agent;
import com.horsecoder.common.whuTalent.core.agent.AgentDescriptor;
import com.horsecoder.common.whuTalent.core.agent.AgentResult;
import com.horsecoder.common.whuTalent.core.agent.AgentTask;
import org.springframework.stereotype.Component;

import java.util.Arrays;
import java.util.Collections;
import java.util.List;
import java.util.Map;

/** Consumes upstream SQL candidates, rejects unsafe statements, and promotes the highest-confidence candidate. */
@Component
public class SqlValidatorAgent implements Agent {
    @Override public String getAgentId() { return "sql-validator"; }
    @Override public AgentDescriptor getDescriptor() {
        return new AgentDescriptor(getAgentId(), "SQL_VALIDATOR", Arrays.asList("sql.validate-readonly", "sql.select-candidate"));
    }
    @Override public AgentResult execute(AgentTask task) {
        Object upstreamObject = task.getContext() == null ? null : task.getContext().get("upstreamResults");
        if (!(upstreamObject instanceof List) || ((List<?>) upstreamObject).isEmpty()) {
            return AgentResult.failure(task.getRequestId(), getAgentId(), "NO_UPSTREAM_CANDIDATE", "sql-validator requires upstreamResults");
        }
        AgentResult best = null;
        for (Object value : (List<?>) upstreamObject) {
            AgentResult candidate = asResult(value);
            if (candidate == null || !"SUCCEEDED".equals(candidate.getStatus()) || !isSafeSelect(candidate.getSql())) continue;
            if (best == null || candidate.getConfidence() > best.getConfidence()) best = candidate;
        }
        if (best == null) return AgentResult.failure(task.getRequestId(), getAgentId(), "NO_VALID_SQL", "No successful read-only SELECT candidate was supplied upstream");
        AgentResult result = new AgentResult();
        result.setRequestId(task.getRequestId()); result.setAgentId(getAgentId()); result.setStatus("SUCCEEDED");
        result.setSql(best.getSql()); result.setParameters(best.getParameters()); result.setRows(best.getRows());
        result.setHitCount(best.getHitCount()); result.setLimitTruncated(best.isLimitTruncated());
        result.setConfidence(best.getConfidence());
        result.setAnswer("Validated and selected the highest-confidence upstream SQL candidate.");
        return result;
    }
    private static AgentResult asResult(Object value) {
        if (value instanceof AgentResult) return (AgentResult) value;
        if (!(value instanceof Map)) return null;
        Map<?, ?> map = (Map<?, ?>) value;
        Object status = map.get("status"), sql = map.get("sql");
        if (status == null || sql == null) return null;
        AgentResult result = new AgentResult();
        result.setStatus(String.valueOf(status)); result.setSql(String.valueOf(sql));
        Object confidence = map.get("confidence");
        if (confidence instanceof Number) result.setConfidence(((Number) confidence).doubleValue());
        return result;
    }
    private static boolean isSafeSelect(String sql) {
        if (sql == null) return false;
        String normalized = sql.trim().toUpperCase(java.util.Locale.ROOT);
        return normalized.startsWith("SELECT ") && normalized.indexOf(';') < 0
                && !normalized.contains(" FOR UPDATE") && !normalized.contains(" INTO OUTFILE")
                && !normalized.contains(" INTO DUMPFILE");
    }
}
