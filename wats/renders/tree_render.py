import os

from wats.files import is_dir, dir_to_string, get_dir_content, file_to_string, get_dir_name, get_file_name


def get_file_size(filepath: str):
    return os.stat(filepath).st_size


def render_file_size(file_size: int):
    return f"{round(file_size / 1024, ndigits=2)} kB"


def render_file(file: tuple):
    return file_to_string(file)


def render_dir(dir: tuple):
    return f"[{dir_to_string(dir)}]"


def make_indent(depth):
    return "--" * depth


def render(tree: tuple, root_path):
    def inner(node, node_path, depth=0):
        indent = make_indent(depth)
        if is_dir(node):
            dir_str = f"{indent}{render_dir(node)}\n"
            content_str = f"\n{indent}".join(inner(child,
                                                   os.path.join(node_path, get_dir_name(node)),
                                                   depth + 1) for child in get_dir_content(node))
            return dir_str + content_str
        else:
            file_size = get_file_size(os.path.join(node_path, get_file_name(node)))
            return f"{indent}{render_file(node)} :: [{render_file_size(file_size)}] "

    return inner(tree, root_path)