package com.horsecoder.common.whuTalent.core.test.agent;

import ch.vorburger.mariadb4j.DB;
import ch.vorburger.mariadb4j.DBConfigurationBuilder;
import com.horsecoder.common.whuTalent.core.agent.AgentResult;
import com.horsecoder.common.whuTalent.core.agent.AgentTask;
import com.horsecoder.common.whuTalent.core.agent.TextGenerationPort;
import com.horsecoder.common.whuTalent.core.agent.single.ReadOnlyQueryExecutor;
import com.horsecoder.common.whuTalent.core.agent.single.SingleTableDataAgent;
import com.horsecoder.common.whuTalent.core.agent.single.SingleTableSchemaProvider;
import com.horsecoder.common.whuTalent.core.agent.single.SingleTableSqlCompiler;
import com.horsecoder.common.whuTalent.core.agent.SingleTableAgentController;
import org.junit.AfterClass;
import org.junit.Assert;
import org.junit.BeforeClass;
import org.junit.Test;
import org.springframework.jdbc.datasource.DataSourceTransactionManager;
import org.springframework.jdbc.datasource.DriverManagerDataSource;

import javax.sql.DataSource;
import java.sql.Connection;
import java.sql.Statement;
import java.net.ServerSocket;

/** Local MariaDB4j E2E: deliberately uses a stub planner and never calls an LLM endpoint. */
public class SingleTableAgentMariaDbIntegrationTest {
    private static DB database;
    private static DataSource dataSource;

    @BeforeClass
    public static void startDatabase() throws Exception {
        DBConfigurationBuilder config = DBConfigurationBuilder.newBuilder();
        try (ServerSocket socket = new ServerSocket(0)) { config.setPort(socket.getLocalPort()); }
        config.setDataDir(System.getProperty("java.io.tmpdir") + "/agent-mariadb4j-e2e");
        database = DB.newEmbeddedDB(config.build());
        database.start();
        database.createDB("agent_e2e");
        int port = database.getConfiguration().getPort();
        DriverManagerDataSource source = new DriverManagerDataSource();
        source.setDriverClassName("com.mysql.cj.jdbc.Driver");
        source.setUrl("jdbc:mysql://127.0.0.1:" + port + "/agent_e2e?useSSL=false&serverTimezone=UTC");
        source.setUsername("root");
        source.setPassword("");
        dataSource = source;
        try (Connection connection = source.getConnection(); Statement statement = connection.createStatement()) {
            statement.execute("CREATE TABLE people (id INT PRIMARY KEY, name VARCHAR(80), city VARCHAR(80))");
            statement.execute("INSERT INTO people VALUES (1, 'Ada', 'London'), (2, 'Grace', 'New York'), (3, 'Alan', 'London')");
        }
    }

    @AfterClass
    public static void stopDatabase() throws Exception {
        if (database != null) database.stop();
    }

    @Test
    public void schemaPlannerCompilerExecutorAgentAndControllerWorkEndToEnd() {
        TextGenerationPort stubPlanner = (system, input) -> "```json\n" +
                "{\"intent\":\"QUERY\",\"clarification\":null,\"column\":\"name\",\"distinct\":false," +
                "\"aggregate\":\"NONE\",\"filters\":[{\"column\":\"city\",\"operator\":\"EQ\",\"value\":\"London\"}]," +
                "\"orderBy\":[],\"limit\":10}\n```";
        SingleTableSchemaProvider schema = new SingleTableSchemaProvider(dataSource, "people");
        SingleTableSqlCompiler compiler = new SingleTableSqlCompiler(100);
        ReadOnlyQueryExecutor executor = new ReadOnlyQueryExecutor(new org.springframework.jdbc.core.JdbcTemplate(dataSource),
                new DataSourceTransactionManager(dataSource), 5);
        SingleTableDataAgent agent = new SingleTableDataAgent(stubPlanner, schema, compiler, executor);
        SingleTableAgentController controller = new SingleTableAgentController(agent);

        AgentTask task = new AgentTask();
        task.setQuestion("Find names in London");
        org.springframework.http.ResponseEntity<AgentResult> response = controller.query(task);

        Assert.assertEquals(200, response.getStatusCodeValue());
        Assert.assertEquals("SUCCEEDED", response.getBody().getStatus());
        Assert.assertEquals(2, response.getBody().getHitCount());
        Assert.assertEquals("Ada", response.getBody().getRows().get(0).get("name"));
        Assert.assertEquals("Alan", response.getBody().getRows().get(1).get("name"));
        Assert.assertTrue(schema.load().getColumns().stream().anyMatch(column -> column.getName().equals("city") && !column.getSampleValues().isEmpty()));
    }
}
