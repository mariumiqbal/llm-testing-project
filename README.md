## What This Project Does
This project is an evaluation framework that tests Claude AI responses 
for structure, safety, and relevance using Python and pytest.
It validates that AI outputs are not empty, contain expected content,
don't include harmful material, and are consistent across multiple calls.

## Why LLM Testing Is Different From Regular API Testing
Traditional APIs return predictable, deterministic responses — 
you can assert exact values. LLMs don't. The same prompt can return 
different responses every time, and the response can be correct in 
format but wrong in content (hallucination). You need new evaluation 
strategies — keyword matching, consistency scoring, safety checks — 
instead of simple equality assertions.

## What I Tested
- Structure: response is not empty, is a string, within length limits
- Safety: response does not contain harmful content, detects refusals
- Relevance: response is on topic, confident, consistent across calls
- Hallucination: same prompt called twice, word overlap scored

## How To Run
# Install dependencies
pip install -r requirements.txt

# Run all tests
pytest -v

## What I Found
AI responses are non-deterministic — the same question gets different 
answers each time. A 200 status code means nothing if the content is 
wrong. Safety checks are critical — without them harmful prompts can 
return dangerous content. Consistency scoring revealed that Claude 
stays on topic reliably but varies in phrasing, which breaks exact 
match assertions.