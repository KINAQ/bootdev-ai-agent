import os

from helpers.get_file_paths import get_file_paths

schema_get_files_info = {
    "type": "function",
    "function": {
        "name": "get_files_info",
        "description": "Lists files in a specified directory relative to the working directory, providing file size and directory status",
        "parameters": {
            "type": "object",
            "properties": {
                "directory": {
                    "type": "string",
                    "description": "Directory path to list files from, relative to the working directory (default is the working directory itself)",
                },
            },
        },
    },
}

def get_files_info(working_directory: str, directory: str = ".") -> str:
    try:

        absolute_path, target_dir = get_file_paths(working_directory, file_path)


        if os.path.commonpath([absolute_path, target_dir]) != absolute_path:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

        if not os.path.isdir(target_dir):
            return f'Error: "{directory}" is not a directory'

        dir_contents = os.listdir(target_dir)

        print(dir_contents)

        result = []
        for i in dir_contents:
            full_path = os.path.join(target_dir, i)

            try:
                result.append(f"{i}: file_size={os.path.getsize(full_path)}, is_dir={os.path.isdir(full_path)}")

            except Exception as e:  # noqa: BLE001
                result.append(f"Error: Could not read {i} ({e})")

        return "\n".join(result)

    except Exception as e:  # noqa: BLE001
        return f"Error: {e}"
