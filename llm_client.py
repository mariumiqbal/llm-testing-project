from anthropic import Anthropic
from dotenv import load_dotenv
import os

load_dotenv()  # loads .env file

client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

def ask_claude(prompt):
    if not prompt:
        raise ValueError("Prompt cannot be empty")
    message = client.messages.create(
        model="claude-haiku-4-5-20251001",
        max_tokens=1024,
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    return message.content[0].text
    
if __name__ == "__main__":
    response = ask_claude("What is the capital of France?")
    print(response) 
