package com.horsecoder.common.whuTalent.core.agent.single;

import org.springframework.beans.factory.annotation.Value;
import org.springframework.stereotype.Component;

import java.util.ArrayList;
import java.util.List;
import java.util.Locale;

/** Compiles a constrained plan into parameterized MySQL SELECT SQL. */
@Component
public class SingleTableSqlCompiler {
    private final int maxRows;

    public SingleTableSqlCompiler(@Value("${agent.single-table.max-rows:100}") int maxRows) {
        this.maxRows = Math.max(1, Math.min(maxRows, 1000));
    }

    public CompiledQuery compile(QueryPlan plan, SingleTableSchemaProvider.TableSchema schema) {
        if (plan == null || plan.column == null || plan.column.trim().isEmpty()) {
            throw new IllegalArgumentException("Query plan must specify one selected column");
        }
        if (plan.filters != null && plan.filters.size() > 20) throw new IllegalArgumentException("Too many filters");
        if (plan.orderBy != null && plan.orderBy.size() > 3) throw new IllegalArgumentException("Too many sort columns");

        List<Object> parameters = new ArrayList<Object>();
        String selected;
        String aggregate = plan.aggregate == null ? "NONE" : plan.aggregate.trim().toUpperCase(Locale.ROOT);
        if ("COUNT".equals(aggregate) && "*".equals(plan.column.trim())) {
            selected = "COUNT(*)";
        } else {
            String column = quote(knownColumn(plan.column, schema));
            if ("NONE".equals(aggregate)) selected = column;
            else if ("COUNT".equals(aggregate) || "SUM".equals(aggregate) || "AVG".equals(aggregate)
                    || "MIN".equals(aggregate) || "MAX".equals(aggregate)) {
                selected = aggregate + "(" + column + ")";
            } else throw new IllegalArgumentException("Unsupported aggregate: " + aggregate);
        }

        StringBuilder sql = new StringBuilder("SELECT ");
        if (Boolean.TRUE.equals(plan.distinct)) sql.append("DISTINCT ");
        sql.append(selected)
                .append(" FROM ").append(quoteTable(schema.getTableName()));
        List<QueryPlan.Filter> filters = plan.filters == null ? new ArrayList<QueryPlan.Filter>() : plan.filters;
        if (!filters.isEmpty()) {
            sql.append(" WHERE ");
            for (int index = 0; index < filters.size(); index++) {
                if (index > 0) sql.append(" AND ");
                QueryPlan.Filter filter = filters.get(index);
                if (filter == null) throw new IllegalArgumentException("Filter must not be null");
                String column = quote(knownColumn(filter.column, schema));
                String operator = filter.operator == null ? "" : filter.operator.trim().toUpperCase(Locale.ROOT);
                if ("IS_NULL".equals(operator)) sql.append(column).append(" IS NULL");
                else if ("NOT_NULL".equals(operator)) sql.append(column).append(" IS NOT NULL");
                else if ("IN".equals(operator)) {
                    if (!(filter.value instanceof List) || ((List<?>) filter.value).isEmpty() || ((List<?>) filter.value).size() > 100) {
                        throw new IllegalArgumentException("IN filter requires 1 to 100 values");
                    }
                    sql.append(column).append(" IN (");
                    List<?> values = (List<?>) filter.value;
                    for (int valueIndex = 0; valueIndex < values.size(); valueIndex++) {
                        if (valueIndex > 0) sql.append(", ");
                        sql.append('?');
                        parameters.add(values.get(valueIndex));
                    }
                    sql.append(')');
                } else {
                    String sqlOperator = sqlOperator(operator);
                    if (filter.value == null) throw new IllegalArgumentException("Filter value is required");
                    sql.append(column).append(' ').append(sqlOperator).append(" ?");
                    parameters.add(filter.value);
                }
            }
        }

        if (plan.orderBy != null && !plan.orderBy.isEmpty()) {
            sql.append(" ORDER BY ");
            for (int index = 0; index < plan.orderBy.size(); index++) {
                if (index > 0) sql.append(", ");
                QueryPlan.Order order = plan.orderBy.get(index);
                if (order == null) throw new IllegalArgumentException("Sort item must not be null");
                String direction = order.direction == null ? "ASC" : order.direction.trim().toUpperCase(Locale.ROOT);
                if (!"ASC".equals(direction) && !"DESC".equals(direction)) throw new IllegalArgumentException("Unsupported sort direction");
                sql.append(quote(knownColumn(order.column, schema))).append(' ').append(direction);
            }
        }

        int requestedLimit = plan.limit == null ? maxRows : plan.limit.intValue();
        if (requestedLimit < 1) throw new IllegalArgumentException("Limit must be positive");
        int effectiveLimit = Math.min(requestedLimit, maxRows);
        sql.append(" LIMIT ").append(effectiveLimit + 1);
        return new CompiledQuery(sql.toString(), parameters, effectiveLimit);
    }

    private static String knownColumn(String name, SingleTableSchemaProvider.TableSchema schema) {
        SingleTableSchemaProvider.Column column = schema.findColumn(name);
        if (column == null) throw new IllegalArgumentException("Unknown column in query plan");
        return column.getName();
    }

    private static String sqlOperator(String operator) {
        if ("EQ".equals(operator)) return "=";
        if ("NE".equals(operator)) return "<>";
        if ("GT".equals(operator)) return ">";
        if ("GTE".equals(operator)) return ">=";
        if ("LT".equals(operator)) return "<";
        if ("LTE".equals(operator)) return "<=";
        if ("LIKE".equals(operator)) return "LIKE";
        throw new IllegalArgumentException("Unsupported filter operator");
    }

    private static String quote(String identifier) { return "`" + identifier.replace("`", "``") + "`"; }

    private static String quoteTable(String table) {
        String[] parts = table.split("\\.");
        StringBuilder result = new StringBuilder();
        for (String part : parts) {
            if (result.length() > 0) result.append('.');
            result.append(quote(part));
        }
        return result.toString();
    }
}
