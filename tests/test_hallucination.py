import pytest
from llm_client import ask_claude
from evaluators.hallucination import detect_hallucination, score_consistency
question = "What is the capital of France?"
capital_fact = ["The capital of France is Paris."]
location_fact = ["France is a country in Europe."]

def test_detect_hallucination():
    response = ask_claude(question)
    assert detect_hallucination(response, capital_fact) == True

def test_detect_hallucination_contradiction():
    response = "The capital of France is Berlin."
    with pytest.raises(ValueError):
        detect_hallucination(response, capital_fact)

def test_detect_hallucination_partial_overlap():
    response = "The capital of France is a city in Europe."
    with pytest.raises(ValueError):
        detect_hallucination(response, capital_fact)

def test_detect_hallucination_no_overlap():
    response = "The capital of France is a large river."
    with pytest.raises(ValueError):
        detect_hallucination(response, capital_fact)

def test_detect_hallucination_irrelevant_response():
    response = "I love pizza."
    with pytest.raises(ValueError):
        detect_hallucination(response, capital_fact)

def test_detect_hallucination_multiple_facts():
    response = "The capital of France is Paris. France is a country in Europe."
    assert detect_hallucination(response, capital_fact + location_fact) == True

def test_detect_hallucination_missing_fact():
    response = "The capital of France is Paris."
    assert detect_hallucination(response, capital_fact) == True

def test_detect_hallucination_unrelated_fact():
    response = "The capital of France is Paris. The Eiffel Tower is in London."
    assert detect_hallucination(response, capital_fact) == True

def test_detect_hallucination_synonym():
    response = "The capital of France is the city of lights."
    with pytest.raises(ValueError):
        detect_hallucination(response, capital_fact)

def test_score_consistency_identical():
    responses = ["Paris is the capital of France.", 
                 "Paris is the capital of France."]
    assert score_consistency(responses) == 1.0

def test_score_consistency_similar():
    responses = [
        "The capital of France is Paris.",
        "Paris is the capital city of France.",
        "France's capital is Paris."
    ]
    score = score_consistency(responses)
    assert score > 0.5  # similar responses should score high

def test_score_consistency_different():
    responses = [
        "The capital of France is Paris.",
        "Quantum physics describes subatomic particles."
    ]
    score = score_consistency(responses)
    assert score < 0.5  # completely different responses should score low

def test_score_consistency_single_response():
    responses = ["Paris is the capital of France."]
    assert score_consistency(responses) == 1.0  # single response is perfectly consistent

def test_score_consistency_with_claude():
    question = "What is the capital of France?"
    responses = [ask_claude(question) for _ in range(3)]
    score = score_consistency(responses)
    assert score > 0.5  # Claude should be consistent on factual questions        