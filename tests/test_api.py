from fastapi.testclient import TestClient
from api import app

client = TestClient(app)

def test_review_code_endpoint_returns_200():
    response = client.post("/review-code", json={"code": "print('Hello, World!')"})
    assert response.status_code == 200
    
def test_review_code_endpoint_returns_quality_score():
    response = client.post("/review-code", json={"code": "print('Hello, World!')"})
    assert "quality_score" in response.json()

def test_review_code_endpoint_returns_issues():
    response = client.post("/review-code", json={"code": "print('Hello, World!')"})
    assert "issues" in response.json()

def test_review_code_endpoint_empty_code():
    response = client.post("/review-code", json={"code": ""})
    assert response.status_code == 400  # FastAPI returns 400 for validation errors