from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from code_review_agent import review_code
from test_generator_agent import generate_tests

app = FastAPI()

class CodeRequest(BaseModel):
    code: str

class TestRequest(BaseModel):
    code: str
    requirements: str

@app.post("/review-code")
def review_code_endpoint(request: CodeRequest):
    try:
        result = review_code(request.code)
        return result
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/generate-tests")
def generate_tests_endpoint(request: TestRequest):
    try:
        result = generate_tests(request.code, request.requirements)
        clean = result.replace("```python", "").replace("```", "").strip()
        return {"tests": clean}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))