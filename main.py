from dotenv import load_dotenv
import os

import anthropic
load_dotenv(".env")
client = anthropic.Anthropic(api_key=os.getenv("CLAUDE_API_KEY"))

while True:
    query = input("You: ")
    with client.messages.stream(
        max_tokens=1024,
        messages=[{"role": "user", "content": query}],
        model="claude-3-5-sonnet-20240620",
    ) as stream:
        for text in stream.text_stream:
            print(text, end="", flush=True)
            
        print()