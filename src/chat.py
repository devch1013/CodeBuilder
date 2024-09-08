from langchain.agents import initialize_agent, Tool
from langchain.llms import Anthropic
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate

import dotenv
import os

dotenv.load_dotenv(".env")
from langchain.chat_models import ChatAnthropic
from langchain.agents import initialize_agent, Tool
from langchain.schema import HumanMessage

# 1. 도구 함수 정의 (이전과 동일)
def search_tool(query):
    return f"검색 결과: {query}에 대한 정보입니다."

def calculator_tool(expression):
    return f"계산 결과: {eval(expression)}"

def weather_tool(location):
    return f"{location}의 날씨: 맑음, 기온 20도"

# 2. Tool 객체로 래핑 (이전과 동일)
tools = [
    Tool(
        name="Search",
        func=search_tool,
        description="인터넷에서 정보를 검색할 때 유용합니다."
    ),
    Tool(
        name="Calculator",
        func=calculator_tool,
        description="수학 계산을 수행할 때 사용합니다."
    ),
    Tool(
        name="Weather",
        func=weather_tool,
        description="특정 지역의 날씨 정보를 얻을 때 사용합니다."
    )
]

# 3. ChatAnthropic 모델을 사용하는 Agent 초기화
chat_model = ChatAnthropic(model="claude-3-5-sonnet-20240620", anthropic_api_key=os.getenv("CLAUDE_API_KEY"))
agent = initialize_agent(tools, chat_model, agent="chat-zero-shot-react-description", verbose=True)

# 4. Agent 실행
result = agent.run("서울의 날씨가 어떤지 알려주세요.")
print(result)