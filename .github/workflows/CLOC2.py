import os


def count_lines_of_code(directories, languages):
    """Counts lines of code and files with specific extensions within directories.

    Args:
        directories: A list of directory paths to search.
        languages: A list of file extensions (e.g., '.py', '.js') to count.

    Returns:
        A list of strings containing code statistics.
    """

    all_files = {}  # Dictionary to store files and their counts per language
    for directory in directories:
        for filename in os.listdir(directory):
            filepath = os.path.join(directory, filename)
            if os.path.isfile(filepath) and filename.lower().endswith(tuple(languages)):
                print(f"Found {filepath} in {directory}")
                lang = os.path.splitext(filepath)[1].lower()
                all_files.setdefault(lang, {'files': 0, 'lines': 0})[
                    'files'] += 1
                all_files[lang]['lines'] += sum(1 for _ in open(filepath, 'r'))

    lines_of_code_text = ["# Code Stats\n\n"]
    total_files = sum(data['files'] for data in all_files.values())
    total_loc = sum(data['lines'] for data in all_files.values())

    for language, data in all_files.items():
        language = language.upper()[1:]  # Remove dot, uppercase extension
        lines_of_code_text.append(f'- {language}:\n')
        lines_of_code_text.append(f'  - Files: {data["files"]}\n')
        lines_of_code_text.append(f'  - Lines: {data["lines"]}\n')

    lines_of_code_text.append(f'- Total:\n')
    lines_of_code_text.append(f'  - Files: {total_files}\n')
    lines_of_code_text.append(f'  - Lines of Code: {total_loc}\n')

    return lines_of_code_text


languages = [".md", ".html"]
# os.chdir('../../')
directories = [os.path.join(os.getcwd(), "docs")]
lines = count_lines_of_code(directories, languages)

with open("README.md", "w") as f:
    f.writelines(lines)
