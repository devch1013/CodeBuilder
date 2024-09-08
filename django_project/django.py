system_prompt = """
You are a professional developer familiar with the Django framework.
You have been tasked with creating a new Django project for a client.
The client has provided you with a detailed specification for the project.

You can answer in the following format.
[
    {{
        "env": "bash",
        "command": "django-admin startproject mysite"
    }},
    {{
        "env": "bash",
        "command": "cd mysite"
    }},
    ...
]

"env" can be "bash" or "python"
Simply put the code you need in the list in the order you need it.
If you need new files or folders, feel free to create them with the bash command. 
All commands use relative paths to the current folder. 
"""


from dotenv import load_dotenv
import os

import anthropic
load_dotenv(".env")
client = anthropic.Anthropic(api_key=os.getenv("CLAUDE_API_KEY"))


# query = input("You: ")
query = "django 프로젝트를 만들고싶어. 간단하게 사용자가 메모를 입력하면 아래에 저장된 메모를 보여주는 페이지를 만들어줘."
context = ""
with client.messages.stream(
    max_tokens=1024,
    messages=[
        {"role": "user", "content": system_prompt},
        {"role": "assistant", "content": "yes i undersatnd. give me an instruction. I will answer in the requested json format."},
        {"role": "user", "content": query},
        { "role": "assistant", "content": "[\n{"},
        ],
    model="claude-3-5-sonnet-20240620",
) as stream:
    for text in stream.text_stream:
        context += text
        print(text, end="", flush=True)
        
with open("django.txt", "w") as f:
    f.write(context)