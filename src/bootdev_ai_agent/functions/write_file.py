import os

from helpers.get_file_paths import get_file_paths


schema_write_file = {
    "type": "function",
    "function": {
        "name": "write_file",
        "description": "Use this tool to create or overwrite the content of a file at a specified file path.",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "The filepath relative to the working directory, e. g. `my_folder/file.txt`.",
                },
                "content": {
                    "type": "string",
                    "description": "The contents of the file as a string."
                },
            },
            "required": [
                "file_path",
                "content",
            ],
        },
    },
}

def write_file(working_directory: str, file_path: str, content: str) -> str:

    try:

        abs_working, abs_file = get_file_paths(working_directory, file_path)

        if os.path.commonpath([abs_working, abs_file]) != abs_working:
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'

        if os.path.isdir(abs_file):
            return f'Error: Cannot write to "{file_path}" as it is a directory'

        os.makedirs(os.path.dirname(abs_file), exist_ok=True)

        with open(abs_file, mode="w", encoding="utf-8") as f:
            f.write(content)

        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'

    except Exception as e:
        return f"Error: {e}"
