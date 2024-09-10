import os
from llm import prompt
import anthropic

def generate_steps(query):

    client = anthropic.Anthropic(api_key=os.getenv("CLAUDE_API_KEY"))
    start_token = "[\n[\""

    message = client.messages.create(
        max_tokens=1024,
        system=prompt.start_project,
        temperature=0.0,
        messages=[
            {"role": "user", "content": query},
            {"role": "assistant", "content": start_token},
        ],
        model="claude-3-5-sonnet-20240620",
    )
        
    return message.content[0].text
