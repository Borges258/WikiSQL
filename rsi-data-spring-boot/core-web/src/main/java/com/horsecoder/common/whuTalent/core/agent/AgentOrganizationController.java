package com.horsecoder.common.whuTalent.core.agent;

import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;

/** HTTP API for submitting explicit 1-1, 1-N, and N-N Agent DAGs. */
@RestController
@RequestMapping("api/agent/organization")
public class AgentOrganizationController {
    private final AgentOrganizationCoordinator coordinator;

    public AgentOrganizationController(AgentOrganizationCoordinator coordinator) {
        this.coordinator = coordinator;
    }

    @GetMapping("/agents")
    public List<AgentDescriptor> listAgents() { return coordinator.listAgents(); }

    @PostMapping("/execute")
    public ResponseEntity<AgentResult> execute(@RequestBody AgentOrganizationTask task) {
        AgentResult result = coordinator.execute(task);
        if ("FAILED".equals(result.getStatus())) {
            HttpStatus status = "INVALID_ORGANIZATION".equals(result.getErrorCode())
                    ? HttpStatus.BAD_REQUEST : HttpStatus.INTERNAL_SERVER_ERROR;
            return new ResponseEntity<AgentResult>(result, status);
        }
        if ("PARTIAL".equals(result.getStatus())) {
            return new ResponseEntity<AgentResult>(result, HttpStatus.MULTI_STATUS);
        }
        return new ResponseEntity<AgentResult>(result, HttpStatus.OK);
    }
}
