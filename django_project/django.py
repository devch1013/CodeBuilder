system_prompt = """
You are a professional developer familiar with the Django framework.
You have been tasked with creating a new Django project for a client.
The client has provided you with a detailed specification for the project.

You need to generate the steps required to complete the project.
There are three steps:
[console, modify, create]
Below is a description of each step.
console: what commands the user needs to use.
modify: what file the should be modified. Don't give the detail code, just the relative path to the file.
create: what folder/file to create with a relative path.

The steps should be ordered according to the format below and told in sequence
{
    console: "django-admin startproject mysite",
    modify: "./mysite/settings.py",
    create: "./mysite/templates/mysite/index.html",
    ...
}
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
        {"role": "assistant", "content": "yes i undersatnd. give me an instruction. I will answer in the requested format."},
        {"role": "user", "content": query},
        { "role": "assistant", "content": "{"},
        ],
    model="claude-3-5-sonnet-20240620",
) as stream:
    for text in stream.text_stream:
        context += text
        print(text, end="", flush=True)
        
with open("django.txt", "w") as f:
    f.write(context)