def is_relevant(response, question):

    if not any(keyword in response.lower() for keyword in question.lower().split()):
        raise ValueError("Response is not relevant to the question")
    return True

def is_confident(response):
    if any(phrase in response.lower() for phrase in ["i'm not sure", "i don't know", "i think", "maybe", "possibly"]):
        raise ValueError("Response contains uncertainty phrases")
    return True

def is_consistent(response1, response2):
    words1 = set(response1.lower().split())
    words2 = set(response2.lower().split())
    
    # find common words
    common = words1.intersection(words2)
    
    # calculate overlap percentage
    overlap = len(common) / max(len(words1), len(words2))
    
    if overlap < 0.3:  # less than 30% overlap
        raise ValueError(f"Responses are inconsistent — only {overlap:.0%} word overlap")
    return True