package com.horsecoder.common.whuTalent.core.agent.single;

import org.springframework.jdbc.core.JdbcTemplate;
import org.springframework.jdbc.core.PreparedStatementSetter;
import org.springframework.jdbc.core.ResultSetExtractor;
import org.springframework.stereotype.Component;
import org.springframework.transaction.PlatformTransactionManager;
import org.springframework.transaction.TransactionDefinition;
import org.springframework.transaction.support.TransactionTemplate;

import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.ResultSetMetaData;
import java.util.ArrayList;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;
import org.springframework.beans.factory.annotation.Value;

/** Executes only compiler-produced statements in a read-only, time-bounded transaction. */
@Component
public class ReadOnlyQueryExecutor {
    private final JdbcTemplate jdbcTemplate;
    private final TransactionTemplate transactionTemplate;
    private final int queryTimeoutSeconds;

    public ReadOnlyQueryExecutor(JdbcTemplate jdbcTemplate,
                                 PlatformTransactionManager transactionManager,
                                 @Value("${agent.single-table.query-timeout-seconds:10}") int queryTimeoutSeconds) {
        this.jdbcTemplate = jdbcTemplate;
        this.queryTimeoutSeconds = Math.max(1, queryTimeoutSeconds);
        this.transactionTemplate = new TransactionTemplate(transactionManager);
        this.transactionTemplate.setReadOnly(true);
        this.transactionTemplate.setTimeout(this.queryTimeoutSeconds);
        this.transactionTemplate.setPropagationBehavior(TransactionDefinition.PROPAGATION_REQUIRED);
    }

    public List<Map<String, Object>> execute(final CompiledQuery query) {
        return transactionTemplate.execute(status -> jdbcTemplate.query(query.getSql(), new PreparedStatementSetter() {
            @Override
            public void setValues(PreparedStatement statement) throws java.sql.SQLException {
                statement.setQueryTimeout(queryTimeoutSeconds);
                for (int index = 0; index < query.getParameters().size(); index++) {
                    statement.setObject(index + 1, query.getParameters().get(index));
                }
            }
        }, new ResultSetExtractor<List<Map<String, Object>>>() {
            @Override
            public List<Map<String, Object>> extractData(ResultSet resultSet) throws java.sql.SQLException {
                List<Map<String, Object>> rows = new ArrayList<Map<String, Object>>();
                ResultSetMetaData metadata = resultSet.getMetaData();
                int columnCount = metadata.getColumnCount();
                while (resultSet.next()) {
                    Map<String, Object> row = new LinkedHashMap<String, Object>();
                    for (int column = 1; column <= columnCount; column++) {
                        row.put(metadata.getColumnLabel(column), resultSet.getObject(column));
                    }
                    rows.add(row);
                }
                return rows;
            }
        }));
    }
}
