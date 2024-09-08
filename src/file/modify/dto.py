from pydantic import BaseModel

class EditFileDto(BaseModel):
    """DTO for editing a file.

    Parameters:
        file_path: Path to the file.
        file_content: Content of the file.
    """

    file_path: str
    line_number: int
    new_text: str