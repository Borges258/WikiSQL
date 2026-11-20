package com.horsecoder.common.whuTalent.core.agent.single;

import java.util.ArrayList;
import java.util.List;

/** Deliberately narrow, structured intent contract; it is not executable SQL. */
public class QueryPlan {
    public String intent;
    public String clarification;
    public String column;
    public String aggregate;
    public Boolean distinct;
    public List<Filter> filters = new ArrayList<Filter>();
    public List<Order> orderBy = new ArrayList<Order>();
    public Integer limit;

    public static class Filter {
        public String column;
        public String operator;
        public Object value;
    }

    public static class Order {
        public String column;
        public String direction;
    }
}
