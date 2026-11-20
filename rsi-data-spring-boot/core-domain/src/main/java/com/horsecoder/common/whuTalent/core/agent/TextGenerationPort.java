package com.horsecoder.common.whuTalent.core.agent;

/** Provider-neutral JSON generation port used by reasoning agents. */
public interface TextGenerationPort {
    String generateJson(String systemInstruction, String userInput);
}
