from llm_client import ask_claude
from evaluators.relevance import is_relevant, is_confident, is_consistent
import pytest

question = "What is the capital of France?"
response1 = ask_claude(question)
response2 = ask_claude(question)  # call twice for consistency check

def test_is_relevant():
    assert is_relevant(response1, question) == True

def test_is_not_relevant():
    with pytest.raises(ValueError):
        is_relevant("I am a doctor", question)

def test_is_confident():
    assert is_confident(response1) == True

def test_is_not_confident():
    with pytest.raises(ValueError):
        is_confident("I'm not sure about that.")


def test_is_consistent():
    assert is_consistent(response1, response2) == True

def test_is_not_consistent():
    with pytest.raises(ValueError):
        is_consistent("The capital of France is Paris.", "Quantum physics describes subatomic particles and wave functions.")