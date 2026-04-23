from test_generator_agent import generate_tests
import pytest

def test_generate_tests_returns_string():
    code = "def add(a, b):\n    return a + b"
    requirements = "- The function should return the sum of two numbers."
    result = generate_tests(code, requirements)
    assert isinstance(result, str)

def test_generate_tests_contains_pytest():
    code = "def add(a, b):\n    return a + b"
    requirements = "- The function should return the sum of two numbers."
    result = generate_tests(code, requirements)
    assert "pytest" in result

def test_generate_tests_contains_assert():
    code = "def add(a, b):\n    return a + b"
    requirements = "- The function should return the sum of two numbers."
    result = generate_tests(code, requirements)
    assert "assert" in result

def test_generate_tests_empty_code_raises():
    with pytest.raises(ValueError):
        generate_tests("", "requirements")

def test_generate_tests_empty_requirements_raises():
    with pytest.raises(ValueError):
        generate_tests("code", "")