import pathlib
from llm_client import ask_claude


def read_rag_sample_data(path="sample_data"):
    """Read RAG sample data from a local file."""
    sample_file = pathlib.Path(path)
    if not sample_file.exists():
        raise FileNotFoundError(f"RAG sample data file not found: {sample_file}")
    return sample_file.read_text(encoding="utf-8")


def ask_from_document(document: str, question: str) -> str:
    if not document:
        raise ValueError("Document cannot be empty")
    if not question:
        raise ValueError("Question cannot be empty")
    prompt = f"""Answer the question using ONLY the information provided in the document below. If the answer is not in the document, say "I don't know".

Document:
{document}

Question:
{question}"""

    return ask_claude(prompt)


def main():
    document = read_rag_sample_data("sample_data.txt")
    
    questions = [
        "Who is the CEO of TechCorp?",
        "Where is the company headquartered?",
        "What products does TechCorp offer?",
        "When was the company founded?",
        "What is the company's stock price?"  # not in document
    ]
    
    for question in questions:
        answer = ask_from_document(document, question)
        print(f"Q: {question}")
        print(f"A: {answer}")
        print("---")


if __name__ == "__main__":
    main()
