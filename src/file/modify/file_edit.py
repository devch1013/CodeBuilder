import json
import os

def modify_file(relative_path, start_line, end_line, new_text):
    """
    파일의 내용을 변경
    """

    # 상대 경로를 절대 경로로 변환
    absolute_path = os.path.abspath(relative_path)

    # 파일 읽기
    with open(absolute_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    # 라인 범위가 유효한지 확인
    if 1 <= start_line <= end_line <= len(lines):
        # 새 텍스트를 줄 단위로 분리
        new_lines = new_text.split('\n')
        
        # 지정된 범위의 라인을 새 텍스트로 교체
        lines[start_line-1:end_line] = [line + '\n' for line in new_lines]

        # 수정된 내용을 파일에 쓰기
        with open(absolute_path, 'w', encoding='utf-8') as file:
            file.writelines(lines)
        
        print(f"파일 {relative_path}의 {start_line}~{end_line} 라인이 성공적으로 수정되었습니다.")
    else:
        print(f"오류: 유효하지 않은 라인 범위입니다. 파일은 {len(lines)}줄입니다.")


if __name__ == '__main__':
    # JSON 입력 예시
    json_input = '''
    {
        "relative_path": "./example.txt",
        "start_line": 10,
        "end_line": 15,
        "new_text": "def new_function():\\n    print('This is a new function')\\n    return True\\n\\n# 이 부분이 새로 추가되었습니다\\nprint('Hello, World!')"
    }
    '''

    # JSON 파싱 및 함수 호출
    file_info = json.loads(json_input)
    modify_file(**file_info)