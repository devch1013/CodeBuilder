import os

import dotenv
import anthropic

from src.file.file_watcher import FileWatcher
from step_manager import StepManager, StepType
from src.llm.llm import LLM, Claude

dotenv.load_dotenv(".env")

class CodeBuilder:
    def __init__(self) -> None:
        self.current_dir = os.getcwd()
        self.llm: LLM = Claude()
        
        self.step_manager = StepManager(self.llm)
        self.file_watcher = FileWatcher(self.current_dir)
        
    def do_next(self):
        step_type, step = self.step_manager.get_next()
        if step_type == StepType.CD:
            self.file_watcher.change_dir(step)
        elif step_type == StepType.COMMAND:
            os.system(step)
        elif step_type == StepType.MODIFY:
            print("modify")
        elif step_type == StepType.CREATE:
            print("create")
        
    def start(self, query):
        self.step_manager.get_step(query)
        
if __name__ == "__main__":
    code_builder = CodeBuilder()
    print(code_builder.current_dir)