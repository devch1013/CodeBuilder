import os

from dotenv import load_dotenv
import anthropic
load_dotenv(".env")

client = anthropic.Anthropic(api_key=os.getenv("CLAUDE_API_KEY"))
