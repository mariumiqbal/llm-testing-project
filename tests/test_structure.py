from llm_client import ask_claude
import pytest
from evaluators.structure import is_not_empty, is_string, contains_keyword, is_within_length

response = ask_claude("What is the capital of France?")

short_response = "Paris"
long_response = "Paris is the capital of France and a beautiful city."

def test_is_not_empty_valid():
    assert is_not_empty(response) == True

def test_is_not_empty_fails_on_empty():
    with pytest.raises(ValueError):
        is_not_empty("")

def test_is_not_empty_fails_on_none():
    with pytest.raises(ValueError):
        is_not_empty(None) 

def test_is_string():
    with pytest.raises(ValueError):
        is_string(123)

def test_contains_keyword():
    contains_keyword(response, "Paris")

def test_is_within_length_valid():
    assert is_within_length(short_response, 100) == True

def test_is_within_length_fails():
    with pytest.raises(ValueError):
        is_within_length(long_response, 5)

def test_valid_response():
    is_not_empty(response)
    is_string(response)
    contains_keyword(response, "Paris")
    is_within_length(response, 1000)

def test_contains_keyword_fails_when_missing():
    with pytest.raises(ValueError):
        contains_keyword(response, "banana")

def test_is_within_length_fails_when_too_long():
    with pytest.raises(ValueError):
        is_within_length(response, 5)            