import subprocess

def bash(text: str):
    """
    use this function to run bash commands
    Example:
    {
        "bash": "django-admin startproject mysite",
        ...
    }
    """
    subprocess.run([text.split()], shell=True)
    
def edit(text: str):
    """
    use this function to edit a file
    Example:
    {
        "edit": {
            "relative_path": "./example.txt",
            "start_line": 10,
            "end_line": 15,
            "new_text": "def new_function():\\n    print('This is a new function')\\n    return True\\n\\n# 이 부분이 새로 추가되었습니다\\nprint('Hello, World!')"
        }, ...
    }
    """
    exec(text)
    
    
