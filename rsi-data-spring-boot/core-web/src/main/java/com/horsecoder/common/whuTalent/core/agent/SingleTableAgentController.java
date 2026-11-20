package com.horsecoder.common.whuTalent.core.agent;

import com.horsecoder.common.whuTalent.core.agent.single.SingleTableDataAgent;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("api/agent/single-table")
public class SingleTableAgentController {
    private final SingleTableDataAgent agent;

    public SingleTableAgentController(SingleTableDataAgent agent) { this.agent = agent; }

    @PostMapping("/query")
    public ResponseEntity<AgentResult> query(@RequestBody AgentTask task) {
        AgentResult result = agent.execute(task);
        if ("FAILED".equals(result.getStatus())) {
            HttpStatus status = "INVALID_REQUEST".equals(result.getErrorCode())
                    ? HttpStatus.BAD_REQUEST
                    : ("PLAN_REJECTED".equals(result.getErrorCode())
                    ? HttpStatus.UNPROCESSABLE_ENTITY : HttpStatus.INTERNAL_SERVER_ERROR);
            return new ResponseEntity<AgentResult>(result, status);
        }
        return new ResponseEntity<AgentResult>(result, HttpStatus.OK);
    }
}
