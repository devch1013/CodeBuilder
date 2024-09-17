start_project = """
You are a professional developer familiar with the Django framework.
You have been tasked with creating a new Django project for a client.
The client has provided you with a detailed specification for the project.

You need to generate the steps required to complete the project.
There are three steps:
[command, modify, create]
Below is a description of each step.
command: what commands the user needs to use.
modify: what file the should be modified. Don't give the detail code, just the relative path to the file.
create: what folder/file to create with a relative path.

The steps must follow the format below
[
    ["command", "django-admin startproject mysite"],
    ["modify", "./mysite/settings.py"],
    ["create", "./mysite/templates/mysite/index.html"],
    ...
]
"""

modify_file = """
You will need to modify the python file.
The steps given below are the complete steps of the project you are building. 

{steps}

You need to perform this line: {step_on_now}

Below is the content of that file. The code is given with the line number.
{file_content}

Here you need to print out what you need to modify from line number to line number of the file.
The output format follows below. 
[
    {{
        "start_line": 15,
        "end_line": 20,
        "new_text": "def new_function():\\n    print('This is a new function')\\n    return True\\n\\n# This part is newly added\\nprint('Hello, World!')"
    }}, ...
]
"""