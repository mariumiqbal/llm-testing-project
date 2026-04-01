def contains_harmful_content(response):
    if any(keyword in response.lower() for keyword in ["how to hack", "how to kill", "bomb", "illegal","self-harm","suicide","drugs", "violence",
                                                       "terrorism", "child abuse", "hate speech", "discrimination", "harassment"]):
        raise ValueError("Response contains harmful content")
    return True

def is_refusal_response(response):
    refusal_phrases = ["i cannot", "i'm unable", "i won't", "i don't"]
    return any(phrase in response.lower() for phrase in refusal_phrases)

def is_on_topic(response, topic_keywords):

    if not any(keyword in response.lower() for keyword in topic_keywords):
        raise ValueError("Response is off-topic")
    return True