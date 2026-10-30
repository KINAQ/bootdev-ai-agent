from functions.get_files_info import get_files_info

test_cases = [
    ("calculator", "."),
    ("calculator", "pkg"),
    ("calculator", "/bin"),
    ("calculator", "../"),
]

for working_dir, operator in test_cases:
    print(f"""
    Result for '{working_dir}' directory:
    {get_files_info(working_dir, operator)}
    """)
