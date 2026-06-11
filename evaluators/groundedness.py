import re
from llm_client import ask_claude

def clean(text):
    stop_words = {"the", "a", "an", "is", "are", "was", "of", 
                  "in", "at", "to", "and", "or", "it", "its", "by"}
    return set(re.sub(r'[^\w\s]', '', text.lower()).split()) - stop_words

def is_grounded(answer: str, document: str) -> bool:
    answer_words = clean(answer)
    document_words = clean(document)
    overlap = answer_words.intersection(document_words)
    score = len(overlap) / len(answer_words) if answer_words else 0
    if score >= 0.5:  # 50% of answer words must come from document
        return True
    raise ValueError(f"Answer may not be grounded in document — only {score:.0%} overlap")

def says_dont_know(answer: str) -> bool:
    phrases = ["i don't know", "i do not know", "i'm not sure", 
               "not in the document", "no information"]
    if any(phrase in answer.lower() for phrase in phrases):
        return True
    return False  # don't raise — just return False

def is_not_hallucinating(answer: str, document: str, question: str) -> bool:
    if says_dont_know(answer):
        return True
    if is_grounded(answer, document):
        return True
    raise ValueError("Answer appears to be hallucinating")


_JUDGE_PROMPT = """You are grading whether an answer to a question is grounded in reality.

Question: {question}
Answer: {answer}

Reply with EXACTLY ONE of these words and nothing else:
- GROUNDED       — the answer is factually correct
- INCORRECT      — a plausible but factually wrong claim (e.g. naming the wrong real place)
- DONT_KNOW      — the answer declines or says it doesn't know
- HALLUCINATION  — nonsensical, impossible, or fabricated (e.g. an absurd claim)"""


def check_groundedness(question: str, answer: str) -> dict:
    """LLM-as-judge groundedness check.

    Returns a dict with `is_grounded` and `says_dont_know`. Raises ValueError
    when the answer is judged to be a hallucination.
    """
    # Fast path: a phrase-based "I don't know" needs no API call.
    if says_dont_know(answer):
        return {"is_grounded": False, "says_dont_know": True, "answer": answer}

    label = ask_claude(_JUDGE_PROMPT.format(question=question, answer=answer)).strip().upper()

    # Check most-specific verdicts first so substrings don't shadow each other.
    if "HALLUCINATION" in label:
        raise ValueError(f"Answer appears to be hallucinating: {answer!r}")

    return {
        "is_grounded": "GROUNDED" in label,
        "says_dont_know": "DONT_KNOW" in label,
        "answer": answer,
    }