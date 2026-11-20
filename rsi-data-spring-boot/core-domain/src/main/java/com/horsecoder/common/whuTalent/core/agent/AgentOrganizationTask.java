package com.horsecoder.common.whuTalent.core.agent;

import java.io.Serializable;
import java.util.ArrayList;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;

/** Client-supplied directed acyclic organization graph for registered agents. */
public class AgentOrganizationTask implements Serializable {
    private static final long serialVersionUID = 1L;

    private String requestId;
    private String question;
    private List<Node> nodes = new ArrayList<Node>();
    private Map<String, Object> context = new LinkedHashMap<String, Object>();
    private Map<String, Object> constraints = new LinkedHashMap<String, Object>();

    public String getRequestId() { return requestId; }
    public void setRequestId(String requestId) { this.requestId = requestId; }
    public String getQuestion() { return question; }
    public void setQuestion(String question) { this.question = question; }
    public List<Node> getNodes() { return nodes; }
    public void setNodes(List<Node> nodes) { this.nodes = nodes; }
    public Map<String, Object> getContext() { return context; }
    public void setContext(Map<String, Object> context) { this.context = context; }
    public Map<String, Object> getConstraints() { return constraints; }
    public void setConstraints(Map<String, Object> constraints) { this.constraints = constraints; }

    public static class Node implements Serializable {
        private static final long serialVersionUID = 1L;

        private String nodeId;
        private String agentId;
        private String question;
        private List<String> dependsOn = new ArrayList<String>();

        public String getNodeId() { return nodeId; }
        public void setNodeId(String nodeId) { this.nodeId = nodeId; }
        public String getAgentId() { return agentId; }
        public void setAgentId(String agentId) { this.agentId = agentId; }
        public String getQuestion() { return question; }
        public void setQuestion(String question) { this.question = question; }
        public List<String> getDependsOn() { return dependsOn; }
        public void setDependsOn(List<String> dependsOn) { this.dependsOn = dependsOn; }
    }
}
