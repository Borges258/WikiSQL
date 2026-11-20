package com.horsecoder.common.whuTalent.core.agent.single;

import org.springframework.beans.factory.annotation.Value;
import org.springframework.stereotype.Component;

import javax.sql.DataSource;
import java.sql.Connection;
import java.sql.DatabaseMetaData;
import java.sql.ResultSet;
import java.sql.PreparedStatement;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.regex.Pattern;

/** Reads only the configured table's schema; no table identifier comes from the model or request. */
@Component
public class SingleTableSchemaProvider {
    private static final Pattern SAFE_IDENTIFIER = Pattern.compile("[A-Za-z0-9_]+(\\.[A-Za-z0-9_]+)?");

    private final DataSource dataSource;
    private final String configuredTable;

    public SingleTableSchemaProvider(
            DataSource dataSource,
            @Value("${agent.single-table.name:}") String configuredTable) {
        this.dataSource = dataSource;
        this.configuredTable = configuredTable == null ? "" : configuredTable.trim();
    }

    public TableSchema load() {
        if (configuredTable.isEmpty()) {
            throw new IllegalStateException("Set agent.single-table.name to the approved business table");
        }
        if (!SAFE_IDENTIFIER.matcher(configuredTable).matches()) {
            throw new IllegalStateException("Configured table name contains unsupported characters");
        }

        try (Connection connection = dataSource.getConnection()) {
            String tableName = configuredTable.substring(configuredTable.lastIndexOf('.') + 1);
            String catalog = configuredTable.contains(".")
                    ? configuredTable.substring(0, configuredTable.lastIndexOf('.'))
                    : connection.getCatalog();
            DatabaseMetaData metadata = connection.getMetaData();
            List<Column> columns = new ArrayList<Column>();
            try (ResultSet resultSet = metadata.getColumns(catalog, null, tableName, null)) {
                while (resultSet.next()) {
                    String columnName = resultSet.getString("COLUMN_NAME");
                    columns.add(new Column(columnName, resultSet.getString("TYPE_NAME"), sampleValues(connection, configuredTable, columnName)));
                }
            }
            if (columns.isEmpty()) {
                throw new IllegalStateException("Configured table was not found or has no visible columns");
            }
            return new TableSchema(configuredTable, columns);
        } catch (Exception exception) {
            if (exception instanceof IllegalStateException) throw (IllegalStateException) exception;
            throw new IllegalStateException("Unable to read configured table schema", exception);
        }
    }

    private static List<Object> sampleValues(Connection connection, String table, String column) throws Exception {
        List<Object> values = new ArrayList<Object>();
        String sql = "SELECT DISTINCT `" + column.replace("`", "``") + "` FROM " + quoteTable(table) + " WHERE `"
                + column.replace("`", "``") + "` IS NOT NULL LIMIT 10";
        try (PreparedStatement statement = connection.prepareStatement(sql)) {
            statement.setQueryTimeout(3);
            try (ResultSet resultSet = statement.executeQuery()) {
                while (resultSet.next()) values.add(resultSet.getObject(1));
            }
        }
        return values;
    }

    private static String quoteTable(String table) {
        StringBuilder quoted = new StringBuilder();
        for (String part : table.split("\\.")) {
            if (quoted.length() > 0) quoted.append('.');
            quoted.append('`').append(part.replace("`", "``")).append('`');
        }
        return quoted.toString();
    }

    public static final class TableSchema {
        private final String tableName;
        private final List<Column> columns;

        public TableSchema(String tableName, List<Column> columns) {
            this.tableName = tableName;
            this.columns = Collections.unmodifiableList(new ArrayList<Column>(columns));
        }
        public String getTableName() { return tableName; }
        public List<Column> getColumns() { return columns; }
        public Column findColumn(String name) {
            if (name == null) return null;
            for (Column column : columns) if (column.getName().equalsIgnoreCase(name)) return column;
            return null;
        }
    }

    public static final class Column {
        private final String name;
        private final String type;
        private final List<Object> sampleValues;
        public Column(String name, String type) { this(name, type, Collections.emptyList()); }
        public Column(String name, String type, List<Object> sampleValues) {
            this.name = name; this.type = type;
            this.sampleValues = Collections.unmodifiableList(new ArrayList<Object>(sampleValues));
        }
        public String getName() { return name; }
        public String getType() { return type; }
        public List<Object> getSampleValues() { return sampleValues; }
    }
}
