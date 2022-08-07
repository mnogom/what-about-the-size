import os


def get_file_size(filepath: str):
    return os.stat(filepath).st_size


def render_file_size(file_size: int):
    return f"{round(file_size / 1024, ndigits=2)} kB"
