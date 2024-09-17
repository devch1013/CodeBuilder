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
        
    def get_step(self, query):
        start_token = "[\n[\""
        result = self.llm.run(prompt.start_project, query, start_token)
        print("result: ", result)
        step_string = start_token + result
        self.steps = extract_list_from_string(step_string)
        return self.steps
    
    def get_next(self) -> Tuple[StepType, str]:
        next_step = self.steps.pop(0)
        if next_step[0] == StepType.MODIFY.value:
            return StepType.MODIFY, next_step[1]
        if next_step[0] == StepType.CREATE.value:
            return StepType.CREATE, next_step[1]
        if next_step[0] == StepType.COMMAND.value:
            if next_step[1].split()[0] == StepType.CD.value:
                return StepType.CD, next_step[2]
        return StepType.COMMAND, next_step[1]
        



if __name__ == "__main__":
    llm = Claude()
    step_manager = StepManager(llm)
    step_manager.get_step("Generate a new django project about memo app")
    print(step_manager.steps)
    
        
        