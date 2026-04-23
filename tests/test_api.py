from fastapi.testclient import TestClient
from api import app

api_client = TestClient(app)

def test_review_code_endpoint_returns_200():
    response = api_client.post("/review-code", json={"code": "print('Hello')"})
    assert response.status_code == 200

def test_review_code_endpoint_returns_quality_score():
    response = api_client.post("/review-code", json={"code": "print('Hello')"})
    assert "quality_score" in response.json()

def test_review_code_endpoint_returns_issues():
    response = api_client.post("/review-code", json={"code": "print('Hello')"})
    assert "issues" in response.json()

def test_review_code_endpoint_empty_code():
    response = api_client.post("/review-code", json={"code": ""})
    assert response.status_code == 400

def test_generate_tests_endpoint_returns_200():
    response = api_client.post("/generate-tests", json={
        "code": "def add(a, b): return a + b",
        "requirements": "Should return sum of two numbers"
    })
    assert response.status_code == 200

def test_generate_tests_endpoint_returns_tests():
    response = api_client.post("/generate-tests", json={
        "code": "def add(a, b): return a + b",
        "requirements": "Should return sum of two numbers"
    })
    assert "tests" in response.json()

def test_generate_tests_endpoint_contains_assert():
    response = api_client.post("/generate-tests", json={
        "code": "def add(a, b): return a + b",
        "requirements": "Should return sum of two numbers"
    })
    assert "assert" in response.json()["tests"]

def test_generate_tests_endpoint_empty_code():
    response = api_client.post("/generate-tests", json={
        "code": "",
        "requirements": "Should return sum"
    })
    assert response.status_code == 400