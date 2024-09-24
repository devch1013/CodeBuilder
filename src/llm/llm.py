import os
import dotenv

dotenv.load_dotenv(".env")

from anthropic import Anthropic
from src.util import extract_list_from_string


class LLM:
    def __init__(self, llm):
        self.llm = llm

    def run(self, system_prompt, query, start_token):
        pass
    
    def parse(self, query):
        pass


class Claude(LLM):
    def __init__(self):
        super().__init__(llm=Anthropic(api_key=os.getenv("CLAUDE_API_KEY")))

    def run(self, system_prompt, query, start_token):
        message = self.llm.messages.create(
            max_tokens=1024,
            system=system_prompt,
            temperature=0.0,
            messages=[
                {"role": "user", "content": query},
                {"role": "assistant", "content": start_token},
            ],
            model="claude-3-5-sonnet-20240620",
        )
        print("LLM response: ", message.content[0].text)
        return extract_list_from_string(start_token+message.content[0].text)
