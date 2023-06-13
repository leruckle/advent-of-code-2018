import pathlib

def read_input_file(input_file_name):
    """Parse the input fie into raw, unformatted lines."""
    input_file = pathlib.Path('data', input_file_name)
    if not input_file.exists():
        raise FileNotFoundError(f"Could not find given file: {input_file}")
    with open(input_file, 'r') as file:
        lines = file.readlines()
    return lines
