package com.horsecoder.common.whuTalent.core.agent.single;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class CompiledQuery {
    private final String sql;
    private final List<Object> parameters;
    private final int rowLimit;

    public CompiledQuery(String sql, List<Object> parameters) {
        this(sql, parameters, Integer.MAX_VALUE);
    }
    public CompiledQuery(String sql, List<Object> parameters, int rowLimit) {
        this.sql = sql;
        this.parameters = Collections.unmodifiableList(new ArrayList<Object>(parameters));
        this.rowLimit = rowLimit;
    }
    public String getSql() { return sql; }
    public List<Object> getParameters() { return parameters; }
    public int getRowLimit() { return rowLimit; }
}
