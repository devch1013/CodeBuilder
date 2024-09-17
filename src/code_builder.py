import os

import dotenv
import anthropic
import subprocess

from src.file.file_watcher import FileWatcher
from src.step_manager import StepManager, StepType
from src.llm.llm import LLM, Claude

dotenv.load_dotenv(".env")

class CodeBuilder:
    def __init__(self) -> None:
        self.current_dir = os.getcwd()
        self.llm: LLM = Claude()
        
        self.step_manager = StepManager(self.llm)
        self.file_watcher = FileWatcher(self.current_dir)
        
    def do_next(self):
        next_step = self.step_manager.get_next()
        step_type, step = next_step
        if step_type == StepType.CD:
            print("cd", step)
            self.file_watcher.change_dir(step)
            os.chdir(step)
        elif step_type == StepType.COMMAND:
            print("command", step)
            subprocess.run(step, shell=True)
        elif step_type == StepType.MODIFY:
            print("modify", step)
        elif step_type == StepType.CREATE:
            print("create", step)
        
    def start(self, query):
        self.step_manager.get_fake_step(query)
        while self.step_manager.check_step():
            self.do_next()
            
        
if __name__ == "__main__":
    code_builder = CodeBuilder()
    print(code_builder.current_dir)
    code_builder.start("Generate a new django project about memo app")