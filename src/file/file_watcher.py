import os
import ast
from src.file.modify.file_edit import modify_file

class FileWatcher:
    def __init__(self, current_dir):
        self.current_dir = current_dir
        os.chdir(current_dir)

    def change_dir(self, relative_path):
        self.current_dir = os.path.join(self.current_dir, relative_path)
        os.chdir(self.current_dir)

    def seek(self, relative_path=""):
        path = os.path.join(self.current_dir, relative_path)
        return self._get_structure(path)

    def _get_structure(self, path):
        if not os.path.isdir(path):
            return None
        
        result = {}
        for item in os.listdir(path):
            item_path = os.path.join(path, item)
            if os.path.isdir(item_path):
                result[item] = self._get_structure(item_path)
            else:
                result[item] = None
        return result

    def print(self, relative_path=""):
        return self._print_structure(self.seek(relative_path=relative_path))

    def _print_structure(self, structure, indent=""):
        result = ""
        for idx, (item, sub_structure) in enumerate(structure.items()):
            if idx == len(structure) - 1:
                prefix = "└── "
                next_indent = indent + "    "
            else:
                prefix = "├── "
                next_indent = indent + "│   "
            
            result += f"{indent}{prefix}{item}\n"
            if sub_structure:
                result += self._print_structure(sub_structure, next_indent)
        return result

    def get_functions(self, file_path):
        full_path = os.path.join(self.current_dir, file_path)
        return self._get_functions_and_docstrings(full_path)

    def get_classes(self, file_path):
        full_path = os.path.join(self.current_dir, file_path)
        return self._get_classes_and_docstrings(full_path)

    def _get_functions_and_docstrings(self, file_path):
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                node = ast.parse(file.read())
        except UnicodeDecodeError:
            # UTF-8로 읽기 실패시 CP949로 시도
            with open(file_path, 'r', encoding='cp949') as file:
                node = ast.parse(file.read())

        functions = {}
        for item in node.body:
            if isinstance(item, ast.FunctionDef):
                functions[item.name] = ast.get_docstring(item)
        return functions

    def _get_classes_and_docstrings(self, file_path):
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                node = ast.parse(file.read())
        except UnicodeDecodeError:
            # UTF-8로 읽기 실패시 CP949로 시도
            with open(file_path, 'r', encoding='cp949') as file:
                node = ast.parse(file.read())

        classes = {}
        for item in node.body:
            if isinstance(item, ast.ClassDef):
                classes[item.name] = ast.get_docstring(item)
        return classes
    
    def modify(self, file, modify_dict: dict):
        modify_file(relative_path=file, **modify_dict)
        
    def get_file_content(self, file_path, with_line_number=False):
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                lines = file.readlines()
            
            if with_line_number:
                # 라인 번호 추가
                numbered_lines = [f"{i+1}: {line.rstrip()}" for i, line in enumerate(lines)]
                content = "\n".join(numbered_lines)
            else:
                # 라인 번호 없이 원본 내용 유지
                content = "".join(lines)
            
            return content
        except FileNotFoundError:
            return f"오류: '{file_path}' 파일을 찾을 수 없습니다."
        

# 사용 예시
if __name__ == "__main__":
    watcher = FileWatcher("E:\playground\CodeBuilder")
    print(watcher.print("src"))

    # 함수와 docstring 가져오기
    functions = watcher.get_functions("src/file/modify/file_edit.py")
    print("Functions:", functions)

    # 클래스와 docstring 가져오기
    classes = watcher.get_classes("src/file/modify/file_edit.py")
    print("Classes:", classes)