steps = [
    ["console", "django-admin startproject memo_project"],
    ["console", "cd memo_project"],
    ["console", "python manage.py startapp memo"],
    ["modify", "./memo_project/settings.py"],
    ["modify", "./memo_project/urls.py"],
    ["create", "./memo/models.py"],
    ["create", "./memo/views.py"],
    ["create", "./memo/urls.py"],
    ["create", "./memo/forms.py"],
    ["create", "./memo/templates/memo/index.html"],
    ["console", "python manage.py makemigrations"],
    ["console", "python manage.py migrate"],
    ["console", "python manage.py runserver"],
]

import subprocess
import os

def create_file(path):
    # 디렉토리가 존재하지 않으면 생성
    directory = os.path.dirname(path)
    os.makedirs(directory, exist_ok=True)
    
    # 파일 생성
    with open(path, 'w') as f:
        pass  # 빈 파일 생성

for step in steps:
    if step[0] == "console":
        print(f"Run the command: {step[1]}")
        if step[1].startswith("cd"):
            os.chdir(step[1].split()[1])
        subprocess.run(step[1].split(), shell=True)
    elif step[0] == "modify":
        print(f"Modify the file: {step[1]}")
    elif step[0] == "create":
        print(f"Create the file or folder: {step[1]}")
        create_file(step[1])
        
class StepProcessor:
    def __init__(self, steps):
        self.steps = steps
        
    def run(self):
        for step in self.steps:
            if step[0] == "console":
                print(f"Run the command: {step[1]}")
                if step[1].startswith("cd"):
                    os.chdir(step[1].split()[1])
                subprocess.run(step[1].split(), shell=True)
            elif step[0] == "modify":
                print(f"Modify the file: {step[1]}")
            elif step[0] == "create":
                print(f"Create the file or folder: {step[1]}")
                create_file(step[1])