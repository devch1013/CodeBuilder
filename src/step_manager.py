import os

from typing import List, Tuple
from enum import Enum

from src.llm import prompt
from src.llm.llm import LLM, Claude
from src.util import extract_list_from_string


class StepType(Enum):
    CD = "cd"
    COMMAND = "command"
    MODIFY = "modify"
    CREATE = "create"


class StepManager:
    def __init__(self, llm: LLM):
        self.llm = llm
        self.steps: List[List[str]] = None
        self.last_steps: List[List[str]] = []

    def get_step(self, query):
        start_token = '[\n["'
        result = self.llm.run(prompt.start_project, query, start_token)
        print("result: ", result)
        # step_string = start_token + result
        # self.steps = extract_list_from_string(result)
        return self.steps

    def get_fake_step(self, query):
        self.steps = [
            ["command", "django-admin startproject memo_project"],
            ["command", "cd memo_project"],
            ["command", "python manage.py startapp memo"],
            ["modify", "./memo_project/settings.py"],
            ["modify", "./memo_project/urls.py"],
            ["create", "./memo/models.py"],
            ["create", "./memo/views.py"],
            ["create", "./memo/urls.py"],
            ["create", "./memo/forms.py"],
            ["create", "./memo/templates/memo/index.html"],
            ["command", "python manage.py makemigrations"],
            ["command", "python manage.py migrate"],
            ["command", "python manage.py runserver"],
        ]

    def check_step(self):
        if self.steps is [] or self.steps is None:
            return False
        return True

    def get_next(self) -> Tuple[StepType, str]:
        if self.steps is [] or self.steps is None:
            return None
        next_step = self.steps.pop(0)
        self.last_steps.append(next_step)
        print("next_step: ", next_step)

        if next_step[0] == StepType.MODIFY.value:
            return StepType.MODIFY, next_step[1]
        if next_step[0] == StepType.CREATE.value:
            return StepType.CREATE, next_step[1]
        if next_step[0] == StepType.COMMAND.value:
            if next_step[1].split()[0] == StepType.CD.value:
                return StepType.CD, next_step[1].split()[1]
        return StepType.COMMAND, next_step[1]
    
    def get_last_steps(self):
        content = ""
        for step in self.last_steps[:-1]:
            content += f"{step[0]}: {step[1]}\n"
        return content
    
    def get_current_step(self):
        return f"{self.last_steps[-1][0]}: {self.last_steps[-1][1]}"


if __name__ == "__main__":
    llm = Claude()
    step_manager = StepManager(llm)
    step_manager.get_step("Generate a new django project about memo app")
    print(step_manager.steps)
