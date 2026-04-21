import json
import re
from llm_client import ask_claude

def review_code(code: str) -> dict:
    if not code:
        raise ValueError("Code cannot be empty")
    
    prompt = f"""Review this Python code and respond ONLY with valid JSON.
No explanation, no markdown backticks, just raw JSON with these fields:
- quality_score (integer 1-10)
- issues (list of strings)
- suggestions (list of strings)  
- summary (one sentence string)
- is_safe (boolean)

Code to review:
{code}"""
    
    response = ask_claude(prompt)
    # strip markdown code blocks if present
    clean = re.sub(r'```json|```', '', response).strip()
    return json.loads(clean)


if __name__ == "__main__":
    sample_code = """
def divide(a, b):
    return a / b
"""
    result = review_code(sample_code)
    print(result)