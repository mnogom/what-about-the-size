import os

from wats.files import (
    make_file, make_dir, get_dir_content, is_dir, get_dir_name, get_file_name
)


def build_tree(root_path, ignore_dirs):
    if os.path.isfile(root_path):
        raise TypeError(f"'{root_path}' is not dir")

    def inner(node_name, fullpath):
        if os.path.isdir(fullpath):
            children = os.listdir(fullpath)
            children = list(
                filter(
                    lambda child: os.path.join(fullpath,
                                               child) not in ignore_dirs,
                    children))
            content = [inner(child,
                             os.path.join(fullpath,
                                          child)) for child in children]
            return make_dir(node_name,
                            content)
        return make_file(node_name)

    return inner(".", root_path)


def sort_tree(dir: tuple, reverse=False):
    content = get_dir_content(dir)
    content_dirs = sorted(
        filter(lambda node: is_dir(node), content),
        key=lambda dir: get_dir_name(dir),
        reverse=reverse)
    content_dirs = [sort_tree(child_content,
                              reverse) for child_content in content_dirs]

    content_files = sorted(
        filter(lambda node: not is_dir(node), content),
        key=lambda file: get_file_name(file),
        reverse=reverse)
    sorted_dir = make_dir(
        get_dir_name(dir), [*content_dirs,
                            *content_files])
    return sorted_dir
