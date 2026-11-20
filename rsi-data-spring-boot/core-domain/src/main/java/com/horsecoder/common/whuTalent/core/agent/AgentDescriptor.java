package com.horsecoder.common.whuTalent.core.agent;

import java.io.Serializable;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

/** Routing metadata for discovery and later 1-1, 1-n, and n-n agent organizations. */
public class AgentDescriptor implements Serializable {
    private static final long serialVersionUID = 1L;

    private final String agentId;
    private final String agentType;
    private final List<String> capabilities;

    public AgentDescriptor(String agentId, String agentType, List<String> capabilities) {
        this.agentId = agentId;
        this.agentType = agentType;
        this.capabilities = Collections.unmodifiableList(new ArrayList<String>(capabilities));
    }
    public String getAgentId() { return agentId; }
    public String getAgentType() { return agentType; }
    public List<String> getCapabilities() { return capabilities; }
}
