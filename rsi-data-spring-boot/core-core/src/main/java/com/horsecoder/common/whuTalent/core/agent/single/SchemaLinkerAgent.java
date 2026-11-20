package com.horsecoder.common.whuTalent.core.agent.single;

import com.horsecoder.common.whuTalent.core.agent.Agent;
import com.horsecoder.common.whuTalent.core.agent.AgentDescriptor;
import com.horsecoder.common.whuTalent.core.agent.AgentResult;
import com.horsecoder.common.whuTalent.core.agent.AgentTask;
import org.springframework.stereotype.Component;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

/** Provides the configured table's schema and bounded value context as an organization node. */
@Component
public class SchemaLinkerAgent implements Agent {
    private final SingleTableSchemaProvider schemaProvider;
    public SchemaLinkerAgent(SingleTableSchemaProvider schemaProvider) { this.schemaProvider = schemaProvider; }
    @Override public String getAgentId() { return "schema-linker"; }
    @Override public AgentDescriptor getDescriptor() {
        return new AgentDescriptor(getAgentId(), "SCHEMA_LINKER", Arrays.asList("schema.inspect", "schema.value-context"));
    }
    @Override public AgentResult execute(AgentTask task) {
        AgentResult result = new AgentResult();
        result.setRequestId(task.getRequestId()); result.setAgentId(getAgentId());
        try {
            SingleTableSchemaProvider.TableSchema schema = schemaProvider.load();
            List<String> fields = new ArrayList<String>();
            for (SingleTableSchemaProvider.Column column : schema.getColumns()) {
                fields.add(column.getName() + " (" + column.getType() + "; samples=" + column.getSampleValues() + ")");
            }
            result.setStatus("SUCCEEDED");
            result.setAnswer("Schema context for " + schema.getTableName() + ": " + fields);
            result.setConfidence(1.0d);
        } catch (Exception exception) {
            return AgentResult.failure(task.getRequestId(), getAgentId(), "SCHEMA_LINK_FAILED", exception.getMessage());
        }
        return result;
    }
}
