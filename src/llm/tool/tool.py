import inspect
from typing import Callable

class Tool:
    def __init__(self, func: Callable):
        self.name = func.__name__
        self.func = func
        self.description = func.__doc__
        self.params = inspect.signature(func).parameters
        
    def run(self, *args, **kwargs):
        return self.func(*args, **kwargs)
    
    def __str__(self):
        return self.description

if __name__ == "__main__":
    # 테스트를 위한 예시 함수
    def example_function(a: int, b: str, c: float = 1.0) -> str:
        """
        이 함수는 예시를 위한 것입니다.
        정수, 문자열, 그리고 선택적으로 실수를 받아 문자열을 반환합니다.
        """
        return f"a: {a}, b: {b}, c: {c}"

    # Tool 인스턴스 생성 및 문자열 표현 출력
    tool = Tool(example_function)
    print(str(tool))