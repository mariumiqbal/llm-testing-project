import pytest
from code_review_agent import review_code

def test_review_code_returns_dict():
    code = "def hello():\n    print('Hello, World!')"
    result = review_code(code)
    assert isinstance(result, dict)

def test_review_code_quality_score():
    code = "def hello():\n    print('Hello, World!')"
    result = review_code(code)
    assert 1 <= result["quality_score"] <= 10

def test_review_code_issues():
    code = "def hello():\n    print('Hello, World!')"
    result = review_code(code)
    assert isinstance(result["issues"], list)

def test_review_code_is_safe_unsafe():
    code = "import os\nos.system('rm -rf /')"
    result = review_code(code)
    assert not result["is_safe"]

def test_review_code_is_safe_safe():
    code = "print('Hello, World!')"
    result = review_code(code)
    assert result["is_safe"]

def test_review_code_empty_raises_value_error():
    with pytest.raises(ValueError):
        review_code("")