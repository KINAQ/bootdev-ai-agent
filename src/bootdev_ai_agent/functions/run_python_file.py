import os
import subprocess
from sys import stderr

from helpers.get_file_paths import get_file_paths


schema_run_python_file = {
    "type": "function",
    "function": {
        "name": "run_python_file",
        "description": "Use this tool to run a Python file from the working directory.",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "The filepath relative to the working directory, e. g. `my_folder/script.py`.",
                },
                "args": {
                    "type": "array",
                    "description": "The arguments used in the command to call the function as a list of strings.",
                    "items": {
                        "type": "string",
                    },
                },
            },
            "required": [
                "file_path",
            ],
        },
    },
}

def run_python_file(
    working_directory: str, file_path: str, args: list[str] | None = None
) -> str:

    try:

        abs_working, abs_file = get_file_paths(working_directory, file_path)

        if os.path.commonpath([abs_working, abs_file]) != abs_working:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

        if not os.path.isfile(abs_file):
            return f'Error: "{file_path}" does not exist or is not a regular file'

        if not abs_file.endswith(".py"):
            return f'Error: "{file_path}" is not a Python file'

        command = ["python", abs_file]

        if args:
            command.extend(args)

        result = subprocess.run(args=command, check=False, cwd=abs_working, text=True, timeout=30, capture_output=True)

        output, errors = result.stdout, result.stderr

        output_string = ""

        return_code = result.returncode

        if return_code != 0:
            output_string += f"Process exited with code {return_code}"

        if not output and not errors:
            output_string += "No output produced"
        else:
            output_string += f"STDOUT: {output}"
            output_string += f"STDERR: {errors}"

        return output_string

    except Exception as e:
        return f"Error: executing python file: {e}"
