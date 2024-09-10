from src.llm.tool.tool import Tool
from src.llm.tool.tool_executor import ToolExecutor
from src.llm.tool.agent_tools import bash, edit

tool = [
    Tool(bash),
    Tool(edit)
]

executor = ToolExecutor(tool)