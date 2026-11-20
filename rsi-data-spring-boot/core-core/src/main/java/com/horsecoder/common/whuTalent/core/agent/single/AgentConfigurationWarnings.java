package com.horsecoder.common.whuTalent.core.agent.single;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.stereotype.Component;

import javax.annotation.PostConstruct;

/** Fails visibly at startup configuration review without preventing non-agent APIs from starting. */
@Component
public class AgentConfigurationWarnings {
    private static final Logger log = LoggerFactory.getLogger(AgentConfigurationWarnings.class);
    private final String table;
    private final String model;
    public AgentConfigurationWarnings(@Value("${agent.single-table.name:}") String table,
                                      @Value("${agent.llm.model:}") String model) {
        this.table = table; this.model = model;
    }
    @PostConstruct
    public void reportMissingConfiguration() {
        if (isBlank(table)) log.warn("Single-table Agent is not ready: configure agent.single-table.name before requests");
        if (isBlank(model)) log.warn("Single-table Agent is not ready: configure agent.llm.model before requests");
    }
    private static boolean isBlank(String value) { return value == null || value.trim().isEmpty(); }
}
