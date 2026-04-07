from evaluators.hallucination import detect_hallucination

response = "The capital of France is Berlin."
known_facts = ["The capital of France is Paris."]

stop_words = {"the", "a", "an", "is", "are", "was", "were", 
              "of", "in", "at", "to", "and", "or", "it", "its"}

fact = known_facts[0]
fact_keywords = set(fact.lower().split()) - stop_words
response_words = set(response.lower().split()) - stop_words
overlap = fact_keywords.intersection(response_words)
score = len(overlap) / len(fact_keywords)

print(f"Fact keywords: {fact_keywords}")
print(f"Response words: {response_words}")
print(f"Overlap: {overlap}")
print(f"Score: {score}")