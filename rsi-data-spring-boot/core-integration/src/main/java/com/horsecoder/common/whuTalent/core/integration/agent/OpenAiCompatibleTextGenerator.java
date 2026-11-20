package com.horsecoder.common.whuTalent.core.integration.agent;

import com.horsecoder.common.whuTalent.core.agent.TextGenerationPort;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.http.HttpEntity;
import org.springframework.http.HttpHeaders;
import org.springframework.http.HttpMethod;
import org.springframework.http.MediaType;
import org.springframework.http.ResponseEntity;
import org.springframework.core.ParameterizedTypeReference;
import org.springframework.stereotype.Component;
import org.springframework.http.client.SimpleClientHttpRequestFactory;
import org.springframework.web.client.RestClientException;
import org.springframework.web.client.RestTemplate;

import java.util.ArrayList;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;

/** OpenAI Chat Completions-compatible adapter. Secrets are supplied by environment/configuration. */
@Component
public class OpenAiCompatibleTextGenerator implements TextGenerationPort {
    private final String baseUrl;
    private final String apiKey;
    private final String model;
    private final String reasoningEffort;
    private final RestTemplate restTemplate;

    public OpenAiCompatibleTextGenerator(
            @Value("${agent.llm.base-url:}") String baseUrl,
            @Value("${agent.llm.api-key:}") String apiKey,
            @Value("${agent.llm.model:}") String model,
            @Value("${agent.llm.reasoning-effort:high}") String reasoningEffort) {
        this.baseUrl = baseUrl;
        this.apiKey = apiKey;
        this.model = model;
        this.reasoningEffort = reasoningEffort;
        SimpleClientHttpRequestFactory requestFactory = new SimpleClientHttpRequestFactory();
        requestFactory.setConnectTimeout(10000);
        requestFactory.setReadTimeout(60000);
        this.restTemplate = new RestTemplate(requestFactory);
    }

    @Override
    public String generateJson(String systemInstruction, String userInput) {
        if (isBlank(baseUrl) || isBlank(apiKey) || isBlank(model)) {
            throw new IllegalStateException("Agent LLM is not configured (agent.llm.base-url/api-key/model)");
        }

        HttpHeaders headers = new HttpHeaders();
        headers.setContentType(MediaType.APPLICATION_JSON);
        headers.setBearerAuth(apiKey);

        Map<String, Object> request = new LinkedHashMap<String, Object>();
        request.put("model", model);
        List<Map<String, String>> messages = new ArrayList<Map<String, String>>();
        messages.add(message("system", systemInstruction));
        messages.add(message("user", userInput));
        request.put("messages", messages);
        request.put("response_format", mapOf("type", "json_object"));
        if (!isBlank(reasoningEffort)) request.put("reasoning_effort", reasoningEffort.trim());

        try {
            ResponseEntity<Map<String, Object>> response = restTemplate.exchange(
                    endpoint(), HttpMethod.POST, new HttpEntity<Map<String, Object>>(request, headers),
                    new ParameterizedTypeReference<Map<String, Object>>() { });
            Object choicesValue = response.getBody() == null ? null : response.getBody().get("choices");
            if (!(choicesValue instanceof List) || ((List<?>) choicesValue).isEmpty()) {
                throw new IllegalStateException("LLM response has no choices");
            }
            Object first = ((List<?>) choicesValue).get(0);
            Object messageValue = first instanceof Map ? ((Map<?, ?>) first).get("message") : null;
            Object content = messageValue instanceof Map ? ((Map<?, ?>) messageValue).get("content") : null;
            if (!(content instanceof String) || isBlank((String) content)) {
                throw new IllegalStateException("LLM response has no JSON text content");
            }
            return (String) content;
        } catch (RestClientException exception) {
            throw new IllegalStateException("LLM request failed: " + exception.getMessage(), exception);
        }
    }

    private String endpoint() {
        String base = baseUrl.trim();
        while (base.endsWith("/")) base = base.substring(0, base.length() - 1);
        return base.endsWith("/chat/completions") ? base : base + "/chat/completions";
    }

    private static Map<String, String> message(String role, String content) {
        Map<String, String> message = new LinkedHashMap<String, String>();
        message.put("role", role);
        message.put("content", content);
        return message;
    }

    private static Map<String, String> mapOf(String key, String value) {
        Map<String, String> map = new LinkedHashMap<String, String>();
        map.put(key, value);
        return map;
    }

    private static boolean isBlank(String value) { return value == null || value.trim().isEmpty(); }
}
