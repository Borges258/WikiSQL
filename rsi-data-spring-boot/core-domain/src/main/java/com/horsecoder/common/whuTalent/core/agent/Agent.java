package com.horsecoder.common.whuTalent.core.agent;

/** Atomic agent contract; organizations can delegate tasks through this interface. */
public interface Agent {
    String getAgentId();
    AgentDescriptor getDescriptor();
    AgentResult execute(AgentTask task);
}
