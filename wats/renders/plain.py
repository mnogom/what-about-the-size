import os

from termcolor import colored, cprint

from wats.files import is_dir, get_dir_name, get_dir_content, get_file_name
from wats.renders.utils import get_file_size, render_file_size

DELIMITER = ":::"


def plain_render(tree: tuple, root_path: str):
    def inner(node, node_path):
        if is_dir(node):
            return "\n".join(inner(child,
                                   os.path.join(node_path, get_dir_name(node))
                                   ) for child in get_dir_content(node))
        else:
            file_path = os.path.join(node_path, get_file_name(node))
            file_size = get_file_size(file_path)
            return f"{file_path.split('.', 1)[1]}{DELIMITER}{file_size}"

    structure = inner(tree, root_path)
    rows = structure.split("\n")
    rows_parsed = [row.split(DELIMITER) for row in rows]
    rows_parsed = [[row[0], int(row[1])] for row in rows_parsed]
    rows_parsed = sorted(rows_parsed, key=lambda row: row[1], reverse=True)

    cprint("\n".join((f"[ {colored(render_file_size(row[1]), 'green')} ]"
                      f" :: {row[0]}") for row in rows_parsed))
