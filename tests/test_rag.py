import pytest
from rag_client import read_rag_sample_data, ask_from_document  

def test_read_rag_sample_data():
    # Test that it reads the file correctly
    content = read_rag_sample_data("sample_data.txt")
    assert "TechCorp" in content     
           
def test_ask_from_document():           
    document = read_rag_sample_data("sample_data.txt")
    
    # Test known question
    answer = ask_from_document(document, "Who is the CEO of TechCorp?")
    assert "Sarah Johnson" in answer # assuming this is the CEO name in the document
    
    # Test unknown question
    answer = ask_from_document(document, "What is the company's stock price?")
    assert "I don't know" in answer

def test_missing_file():
    with pytest.raises(FileNotFoundError):
        read_rag_sample_data("non_existent_file.txt")

def test_empty_question():    
    document = read_rag_sample_data("sample_data.txt")
    with pytest.raises(ValueError):       
        ask_from_document(document, "")                 