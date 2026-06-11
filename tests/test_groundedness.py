import pytest
from evaluators.groundedness import check_groundedness, is_grounded, says_dont_know


def test_check_groundedness_returns_dict():
    response = check_groundedness("What is the capital of France?", "The capital of France is Paris.")
    assert isinstance(response, dict)

def test_check_groundedness_correct_answer():
    response = check_groundedness("What is the capital of France?", "The capital of France is Paris.")
    assert response["is_grounded"] == True

def test_check_groundedness_incorrect_answer():
    response = check_groundedness("What is the capital of France?", "The capital of France is Berlin.")
    assert response["is_grounded"] == False

def test_check_groundedness_dont_know():
    response = check_groundedness("What is the capital of France?", "I don't know.")
    assert response["says_dont_know"] == True   

def test_check_groundedness_hallucinating():
    with pytest.raises(ValueError):
        check_groundedness("What is the capital of France?", "The capital of France is a purple elephant that sings opera.")

