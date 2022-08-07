import os

from termcolor import colored, cprint

from wats.files import (
    is_dir, dir_to_string, get_dir_content, file_to_string,
    get_dir_name, get_file_name, is_empty_dir
)
from wats.renders.utils import get_file_size, render_file_size

LINE_SYMBOL = "│"
STRUCTURE_SYMBOL = "├─"
DOT_SYMBOL = colored("•", "green")
EMPTY_SYMBOL = colored("• empty", "red")


def render_file(file: tuple):
    return file_to_string(file)


def render_dir(dir: tuple):
    return f"{dir_to_string(dir)}"


def make_indent(depth: int):
    return f"{LINE_SYMBOL}  " * depth


def tree_render(tree: tuple, root_path: str):
    def inner(node: tuple, node_path: str, depth=0):
        indent = make_indent(depth)
        if is_dir(node):
            dir_str = f"{indent}{STRUCTURE_SYMBOL} {render_dir(node)}\n"
            if is_empty_dir(node):
                content_str = f"{make_indent(depth + 1)}{EMPTY_SYMBOL}"
            else:
                content_str = "\n".join(inner(child,
                                              os.path.join(node_path,
                                                           get_dir_name(node)),
                                              depth + 1)
                                        for child in get_dir_content(node))
            return dir_str + content_str
        else:
            file_size = get_file_size(os.path.join(node_path,
                                                   get_file_name(node)))
            return (f"{indent}{DOT_SYMBOL} {render_file(node)}"
                    f" :: [ {colored(render_file_size(file_size), 'green')} ]")

    cprint(inner(tree, root_path))
