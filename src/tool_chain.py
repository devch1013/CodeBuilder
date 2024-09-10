from src.llm.tool.tool import Tool
from typing import List, Any

class ToolAgent:
    def __init__(self, tools: List[Tool], client: Any) -> None:
        self.tools = tools
        self.client = client
        
    