from dotenv import load_dotenv
from src.generate_steps import generate_steps

load_dotenv(".env")

query = "django 프로젝트를 만들고싶어. 간단하게 사용자가 메모를 입력하면 아래에 저장된 메모를 보여주는 페이지를 만들어줘."

steps = generate_steps(query)

with open("start_project.txt", "w") as f:
    f.write(steps)