import re

def score_consistency(responses):
    # takes a list of responses to the same question
    # compares each response against all others
    # returns a score between 0 and 1
    # 1 = perfectly consistent, 0 = completely different
    total_pairs = 0
    consistent_pairs = 0
    is_consistent=lambda r1, r2: len(set(r1.lower().split()).intersection(set(r2.lower().split()))) / max(len(set(r1.lower().split())), len(set(r2.lower().split()))) >= 0.3
    for i in range(len(responses)):
        for j in range(i + 1, len(responses)):
            total_pairs += 1
            if is_consistent(responses[i], responses[j]):
                consistent_pairs += 1
    if total_pairs == 0:
        return 1.0  # if only one response, consider it perfectly consistent
    return consistent_pairs / total_pairs if total_pairs > 0 else 0.0


def detect_hallucination(response, known_facts):
    stop_words = {"the", "a", "an", "is", "are", "was", "were", 
                  "of", "in", "at", "to", "and", "or", "it", "its"}
    
    def clean(text):
        return set(re.sub(r'[^\w\s]', '', text.lower()).split()) - stop_words
    
    for fact in known_facts:
        fact_keywords = clean(fact)
        response_words = clean(response)
        overlap = fact_keywords.intersection(response_words)
        if len(overlap) / len(fact_keywords) < 0.8:
            raise ValueError(f"Response may contradict known fact: '{fact}'")
    return True
