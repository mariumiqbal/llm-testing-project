from llm_client import ask_claude

def generate_tests(code: str, requirements: str) -> str:

    if not code:
        raise ValueError("Code cannot be empty")
    if not requirements:
        raise ValueError("Requirements cannot be empty")

    prompt = f"""Generate pytest test code for this Python function based on the following requirements.
{code}  
Requirements:
{requirements}      
Only return valid pytest test code. Do not include any explanations or markdown formatting. Just raw code."""
    response = ask_claude(prompt)
    return response.strip() 

if __name__ == "__main__":
    sample_code = """def add(a, b): 
    return a + b
"""
    sample_requirements = """- The function should return the sum of two numbers.
- The function should raise a TypeError if either argument is not a number."""
    tests = generate_tests(sample_code, sample_requirements)
    print(tests)
