# LLM Testing & Evaluation Framework

A Python-based AI evaluation framework that tests Claude API responses 
for structure, safety, relevance, and hallucination. Also includes 
AI-powered agents for code review and test generation, served via FastAPI.

## Why LLM Testing Is Different From Regular API Testing
Traditional APIs return predictable, deterministic responses — you can 
assert exact values. LLMs don't. The same prompt returns different 
responses every time, and a response can be correct in format but wrong 
in content (hallucination). You need new evaluation strategies — keyword 
matching, consistency scoring, safety checks — instead of simple equality 
assertions.

## Evaluators
- **Structure** — response is not empty, is a string, within length limits, contains expected keywords
- **Safety** — detects harmful content, checks for appropriate refusals
- **Relevance** — response is on topic, confident, consistent across calls
- **Hallucination** — word overlap scoring across multiple responses, stop word filtering, punctuation cleaning

## AI Agents
- **Code Review Agent** — sends Python code to Claude, returns structured JSON review with quality score, issues, and suggestions
- **Test Generator Agent** — sends a function + requirements to Claude, returns pytest test code

## API Endpoints

### POST /review-code
Request:
```json
{
  "code": "def divide(a, b):\n    return a / b"
}
```
Response:
```json
{
  "quality_score": 3,
  "issues": ["No division by zero handling"],
  "suggestions": ["Add check for b == 0"],
  "summary": "Function lacks error handling",
  "is_safe": false
}
```

### POST /generate-tests
Request:
```json
{
  "code": "def add(a, b):\n    return a + b",
  "requirements": "Should return sum of two numbers"
}
```
Response:
```json
{
  "tests": "def test_add_positive():\n    assert add(2, 3) == 5\n..."
}
```

## How to Run
# Install dependencies
pip install -r requirements.txt

# Run all tests
pytest -v

# Start API server
uvicorn api:app --reload

# View API docs
http://127.0.0.1:8000/docs

## Tech Stack
- Python 3.11
- pytest
- Claude API (Anthropic)
- FastAPI + uvicorn
- GitHub Actions CI

## What I Found
- AI responses are non-deterministic — same question, different answer every time
- A 200 status code means nothing if the content is wrong
- Keyword matching fails for negation — "Paris is not the capital" still contains "Paris"
- Stop words inflate consistency scores — must filter before comparing
- Claude-generated code can hallucinate imports that don't exist
- Consistency scoring with set intersection works well for factual questions

## Tests
- 55 tests passing
- GitHub Actions CI — all green on every push