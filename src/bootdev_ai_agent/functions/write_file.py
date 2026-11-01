import os

from helpers.get_file_paths import get_file_paths


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
