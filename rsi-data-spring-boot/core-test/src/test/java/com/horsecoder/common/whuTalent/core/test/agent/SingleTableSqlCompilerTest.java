package com.horsecoder.common.whuTalent.core.test.agent;

import com.horsecoder.common.whuTalent.core.agent.single.CompiledQuery;
import com.horsecoder.common.whuTalent.core.agent.single.QueryPlan;
import com.horsecoder.common.whuTalent.core.agent.single.SingleTableSchemaProvider;
import com.horsecoder.common.whuTalent.core.agent.single.SingleTableSqlCompiler;
import org.junit.Assert;
import org.junit.Test;

import java.util.Arrays;
import java.util.Collections;

public class SingleTableSqlCompilerTest {
    private final SingleTableSqlCompiler compiler = new SingleTableSqlCompiler(100);
    private final SingleTableSchemaProvider.TableSchema schema = new SingleTableSchemaProvider.TableSchema(
            "sales.orders", Arrays.asList(
                    new SingleTableSchemaProvider.Column("customer_name", "varchar"),
                    new SingleTableSchemaProvider.Column("amount", "decimal")));

    @Test
    public void compilesOnlyKnownIdentifiersAndBindsValues() {
        QueryPlan plan = new QueryPlan();
        plan.column = "amount";
        plan.aggregate = "SUM";
        QueryPlan.Filter filter = new QueryPlan.Filter();
        filter.column = "customer_name";
        filter.operator = "EQ";
        filter.value = "x' OR 1=1 --";
        plan.filters.add(filter);
        plan.limit = 10000;

        CompiledQuery query = compiler.compile(plan, schema);

        Assert.assertEquals("SELECT SUM(`amount`) FROM `sales`.`orders` WHERE `customer_name` = ? LIMIT 101", query.getSql());
        Assert.assertEquals(100, query.getRowLimit());
        Assert.assertEquals(Arrays.<Object>asList("x' OR 1=1 --"), query.getParameters());
    }

    @Test(expected = IllegalArgumentException.class)
    public void rejectsColumnsOutsideConfiguredSchema() {
        QueryPlan plan = new QueryPlan();
        plan.column = "other_table.secret";
        plan.aggregate = "NONE";
        compiler.compile(plan, schema);
    }

    @Test(expected = IllegalArgumentException.class)
    public void rejectsUnsupportedOperators() {
        QueryPlan plan = new QueryPlan();
        plan.column = "amount";
        plan.aggregate = "NONE";
        QueryPlan.Filter filter = new QueryPlan.Filter();
        filter.column = "amount";
        filter.operator = "OR 1=1";
        filter.value = 0;
        plan.filters.add(filter);
        compiler.compile(plan, schema);
    }

    @Test
    public void compilesInFilterAsBoundParameters() {
        QueryPlan plan = new QueryPlan();
        plan.column = "customer_name";
        plan.aggregate = "NONE";
        QueryPlan.Filter filter = new QueryPlan.Filter();
        filter.column = "amount";
        filter.operator = "IN";
        filter.value = Arrays.<Object>asList(10, 20);
        plan.filters.add(filter);

        CompiledQuery query = compiler.compile(plan, schema);

        Assert.assertEquals("SELECT `customer_name` FROM `sales`.`orders` WHERE `amount` IN (?, ?) LIMIT 101", query.getSql());
        Assert.assertEquals(Arrays.<Object>asList(10, 20), query.getParameters());
    }

    @Test
    public void supportsDistinctSelection() {
        QueryPlan plan = new QueryPlan();
        plan.column = "customer_name";
        plan.distinct = true;
        CompiledQuery query = compiler.compile(plan, schema);
        Assert.assertEquals("SELECT DISTINCT `customer_name` FROM `sales`.`orders` LIMIT 101", query.getSql());
    }

    @Test(expected = IllegalArgumentException.class)
    public void rejectsNullFilterEntries() {
        QueryPlan plan = new QueryPlan();
        plan.column = "amount";
        plan.aggregate = "NONE";
        plan.filters = Collections.singletonList(null);
        compiler.compile(plan, schema);
    }
}
