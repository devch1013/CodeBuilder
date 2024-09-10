from pydantic import BaseModel

class EditFileDto(BaseModel):
    """DTO for editing a file.

    Parameters:
        file_path: Path to the file. (relative)
        line_number: Line number to edit.
        new_text: New text to replace the line with.
    """

    file_path: str
    start_line: int
    end_line: int
    new_text: str