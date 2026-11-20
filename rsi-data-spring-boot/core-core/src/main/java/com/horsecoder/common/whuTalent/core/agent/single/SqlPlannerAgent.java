package com.horsecoder.common.whuTalent.core.agent.single;

import com.horsecoder.common.whuTalent.core.agent.Agent;
import com.horsecoder.common.whuTalent.core.agent.AgentDescriptor;
import com.horsecoder.common.whuTalent.core.agent.AgentResult;
import com.horsecoder.common.whuTalent.core.agent.AgentTask;
import org.springframework.stereotype.Component;

import java.util.Arrays;

/** Organization-facing SQL planning role backed by the validated single-table pipeline. */
@Component
public class SqlPlannerAgent implements Agent {
    private final SingleTableDataAgent dataAgent;
    public SqlPlannerAgent(SingleTableDataAgent dataAgent) { this.dataAgent = dataAgent; }
    @Override public String getAgentId() { return "sql-planner"; }
    @Override public AgentDescriptor getDescriptor() {
        return new AgentDescriptor(getAgentId(), "SQL_PLANNER", Arrays.asList("sql.plan", "sql.execute-readonly"));
    }
    @Override public AgentResult execute(AgentTask task) {
        AgentResult result = dataAgent.execute(task);
        result.setAgentId(getAgentId());
        return result;
    }
}
