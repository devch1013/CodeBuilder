from src.file.file_watcher import FileWatcher
from enum import Enum
import subprocess
from src.llm.tool.tool import Tool
from typing import List, Any

class Command(Enum):
    BASH = "bash"
    PYTHON = "python"
    FILE_EDIT = "file_edit"


class ToolExecutor:
    def __init__(self, tools: List[Tool]) -> None:
        self.file_watcher = FileWatcher(current_dir="./")
        self.tools = tools
        
    def gateway(self, command: str, value: Any):
        for tool in self.tools:
            if tool.name == command:
                tool.run(value)
                return