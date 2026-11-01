import os

from config import FILE_CHARACTER_LIMIT


def get_file_content(working_directory: str, file_path: str) -> str:

    try:

        abs_working = os.path.abspath(working_directory)
        combined = os.path.join(working_directory, file_path)
        abs_file = os.path.abspath(combined)

        if os.path.commonpath([abs_working, abs_file]) != abs_working:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

        if not os.path.isfile(abs_file):
            return f'Error: File not found or is not a regular file: "{file_path}"'

        with open(abs_file, mode="r") as f:
            file_content = f.read(FILE_CHARACTER_LIMIT)

            if f.read(1):
                file_content += f'[...File "{file_path}" truncated at {FILE_CHARACTER_LIMIT} characters]'

        return file_content

    except Exception as e:
        return f"Error: {e}"
