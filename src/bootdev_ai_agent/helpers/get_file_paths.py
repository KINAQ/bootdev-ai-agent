import os


def get_file_paths(working_directory: str, file_path: str) -> tuple[str, str]:
    abs_working = os.path.abspath(working_directory)
    combined = os.path.join(working_directory, file_path)
    abs_file = os.path.abspath(combined)
    return (abs_working, abs_file)
