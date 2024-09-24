import json
# import ast
import re

def extract_list_from_string(input_string):
    # 첫 번째 '[' 와 마지막 ']'의 인덱스를 찾습니다
    start_index = input_string.find('[')
    end_index = input_string.rfind(']')

    if start_index == -1 or end_index == -1:
        return None  # 유효한 리스트가 없음

    # 추출된 문자열을 가져옵니다
    list_string = input_string[start_index:end_index + 1]
    json_string = re.sub(r'(?<!\\)\\n', r'\\n', list_string)
        
        # "new_text" 필드 내의 실제 줄바꿈을 \\n으로 대체
    json_string = re.sub(r'("new_text":\s*")(.+?)(")', 
                            lambda m: m.group(1) + m.group(2).replace('\n', '\\n') + m.group(3), 
                            json_string, flags=re.DOTALL)
    
    try:
        # JSON 파서를 사용하여 문자열을 리스트로 변환합니다
        result = json.loads(json_string)
        if isinstance(result, list):
            return result
        else:
            return None  # 파싱된 결과가 리스트가 아님
    except json.JSONDecodeError as e:
        print(e.msg)
        return None  # JSON 파싱 실패

if __name__ == "__main__":
    # 테스트
    test_string = """[
{"start_line": 33,
"end_line": 41,
"new_text": "INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'memo',  # Add this line
]"},
{"start_line": 33,
"end_line": 41,
"new_text": "INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'memo',  # Add this line
]"},
{"start_line": 33,
"end_line": 41,
"new_text": "INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'memo',  # Add this line
]"}
]"""

    result = extract_list_from_string(test_string)
    print(result)
    
