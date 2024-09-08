import json
import os

def modify_file(file_info):
    relative_path = file_info['relative_path']
    line_number = file_info['line_number']
    new_text = file_info['new_text']

    # 상대 경로를 절대 경로로 변환
    absolute_path = os.path.abspath(relative_path)

    # 파일 읽기
    with open(absolute_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    # 라인 번호가 유효한지 확인
    if 1 <= line_number <= len(lines):
        # 해당 라인 수정
        lines[line_number - 1] = new_text + '\n'

        # 수정된 내용을 파일에 쓰기
        with open(absolute_path, 'w', encoding='utf-8') as file:
            file.writelines(lines)
        
        print(f"파일 {relative_path}의 {line_number}번째 라인이 성공적으로 수정되었습니다.")
    else:
        print(f"오류: {line_number}는 유효하지 않은 라인 번호입니다.")

# JSON 입력 예시
json_input = '''
{
    "relative_path": "./example.txt",
    "line_number": 3,
    "new_text": "이 줄은 수정되었습니다."
}
'''

# JSON 파싱 및 함수 호출
file_info = json.loads(json_input)
modify_file(file_info)