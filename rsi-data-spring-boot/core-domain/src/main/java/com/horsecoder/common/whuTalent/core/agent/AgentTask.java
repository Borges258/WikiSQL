package com.horsecoder.common.whuTalent.core.agent;

import java.io.Serializable;
import java.util.LinkedHashMap;
import java.util.Map;

/** A transport-neutral unit of work that can be delegated between agents. */
public class AgentTask implements Serializable {
    private static final long serialVersionUID = 1L;

    private String requestId;
    private String question;
    private Map<String, Object> context = new LinkedHashMap<String, Object>();
    private Map<String, Object> constraints = new LinkedHashMap<String, Object>();

    public String getRequestId() { return requestId; }
    public void setRequestId(String requestId) { this.requestId = requestId; }
    public String getQuestion() { return question; }
    public void setQuestion(String question) { this.question = question; }
    public Map<String, Object> getContext() { return context; }
    public void setContext(Map<String, Object> context) { this.context = context; }
    public Map<String, Object> getConstraints() { return constraints; }
    public void setConstraints(Map<String, Object> constraints) { this.constraints = constraints; }
}
