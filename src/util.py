import json


def extract_list_from_string(input_string):
    # 첫 번째 '[' 와 마지막 ']'의 인덱스를 찾습니다
    start_index = input_string.find('[')
    end_index = input_string.rfind(']')

    if start_index == -1 or end_index == -1:
        return None  # 유효한 리스트가 없음

    # 추출된 문자열을 가져옵니다
    list_string = input_string[start_index:end_index + 1]

    try:
        # JSON 파서를 사용하여 문자열을 리스트로 변환합니다
        result = json.loads(list_string)
        if isinstance(result, list):
            return result
        else:
            return None  # 파싱된 결과가 리스트가 아님
    except json.JSONDecodeError:
        return None  # JSON 파싱 실패

if __name__ == "__main__":
    # 테스트
    test_string = """이ㅇㅁㅇㄴㅁㅇㄴ[
    ["create", "./memo/templates/memo/base.html"],
    ["create", "./memo/templates/memo/memo_list.html"],
    ["create", "./memo/templates/memo/memo_detail.html"],
    ["create", "./memo/templates/memo/memo_form.html"],
    ["create", "./memo/static/memo/css/style.css"],
    ["console", "python manage.py makemigrations"],
    ["console", "python manage.py migrate"],
    ["console", "python manage.py createsuperuser"],
    ["console", "python manage.py runserver"]
    ]ㅁㄴㅇㅁㄴㅇㅁㄴㅇ"""

    result = extract_list_from_string(test_string)
    print(result)