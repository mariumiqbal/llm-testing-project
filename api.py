from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from code_review_agent import review_code

app = FastAPI()

class CodeRequest(BaseModel):
    code: str

@app.post("/review-code")
def review_code_endpoint(request: CodeRequest):
    try:
        result = review_code(request.code)
        return result
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))