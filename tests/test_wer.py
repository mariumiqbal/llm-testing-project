from evaluators.wer import calculate_wer
import pytest

def test_perfect_match():
    # identical strings should give WER 0.0
    assert calculate_wer("I live in Chicago", "I live in Chicago") == 0.0
def test_one_substitution():
    # "I live in Chicago" vs "I love in Chicago" = 1/4 = 0.25
    assert calculate_wer("I live in Chicago", "I love in Chicago") == 0.25

def test_one_deletion():
    # "I live in Chicago" vs "I live Chicago" = 1/4 = 0.25
    assert calculate_wer("I live in Chicago", "I live Chicago") == 0.25

def test_known_example():
    # our manual calculation — should give 0.5
    assert calculate_wer("I live in Chicago", "I love Chicago") == 0.5

def test_empty_reference_raises():
    # empty reference should raise ValueError
    with pytest.raises(ValueError):
        calculate_wer("", "I live in Chicago")

def test_empty_hypothesis_raises():
    # empty hypothesis should raise ValueError
    with pytest.raises(ValueError):
        calculate_wer("I live in Chicago", "")