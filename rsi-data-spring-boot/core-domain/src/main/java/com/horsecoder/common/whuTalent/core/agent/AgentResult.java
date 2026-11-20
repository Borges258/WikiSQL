package com.horsecoder.common.whuTalent.core.agent;

import java.io.Serializable;
import java.util.ArrayList;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;

/** Stable result envelope for atomic agents and future agent organizations. */
public class AgentResult implements Serializable {
    private static final long serialVersionUID = 1L;

    private String requestId;
    private String agentId;
    private String status;
    private String answer;
    private String sql;
    private List<Object> parameters = new ArrayList<Object>();
    private List<Map<String, Object>> rows = new ArrayList<Map<String, Object>>();
    private long elapsedMs;
    private int hitCount;
    private boolean limitTruncated;
    private double confidence;
    private String errorCode;
    private String errorMessage;
    private String organizationNodeId;
    private String organizationType;
    private List<AgentResult> subResults = new ArrayList<AgentResult>();

    public String getRequestId() { return requestId; }
    public void setRequestId(String requestId) { this.requestId = requestId; }
    public String getAgentId() { return agentId; }
    public void setAgentId(String agentId) { this.agentId = agentId; }
    public String getStatus() { return status; }
    public void setStatus(String status) { this.status = status; }
    public String getAnswer() { return answer; }
    public void setAnswer(String answer) { this.answer = answer; }
    public String getSql() { return sql; }
    public void setSql(String sql) { this.sql = sql; }
    public List<Object> getParameters() { return parameters; }
    public void setParameters(List<Object> parameters) { this.parameters = parameters; }
    public List<Map<String, Object>> getRows() { return rows; }
    public void setRows(List<Map<String, Object>> rows) { this.rows = rows; }
    public long getElapsedMs() { return elapsedMs; }
    public void setElapsedMs(long elapsedMs) { this.elapsedMs = elapsedMs; }
    public int getHitCount() { return hitCount; }
    public void setHitCount(int hitCount) { this.hitCount = hitCount; }
    public boolean isLimitTruncated() { return limitTruncated; }
    public void setLimitTruncated(boolean limitTruncated) { this.limitTruncated = limitTruncated; }
    public double getConfidence() { return confidence; }
    public void setConfidence(double confidence) { this.confidence = confidence; }
    public String getErrorCode() { return errorCode; }
    public void setErrorCode(String errorCode) { this.errorCode = errorCode; }
    public String getErrorMessage() { return errorMessage; }
    public void setErrorMessage(String errorMessage) { this.errorMessage = errorMessage; }
    public String getOrganizationNodeId() { return organizationNodeId; }
    public void setOrganizationNodeId(String organizationNodeId) { this.organizationNodeId = organizationNodeId; }
    public String getOrganizationType() { return organizationType; }
    public void setOrganizationType(String organizationType) { this.organizationType = organizationType; }
    public List<AgentResult> getSubResults() { return subResults; }
    public void setSubResults(List<AgentResult> subResults) { this.subResults = subResults; }

    public static AgentResult failure(String requestId, String agentId, String code, String message) {
        AgentResult result = new AgentResult();
        result.setRequestId(requestId);
        result.setAgentId(agentId);
        result.setStatus("FAILED");
        result.setErrorCode(code);
        result.setErrorMessage(message);
        return result;
    }
}
