def make_dir(name: str, content=None):
    return name, content if content else []


def get_dir_name(dir: tuple):
    return dir[0]


def get_dir_content(dir: tuple):
    return dir[1]


def is_empty_dir(dir: tuple):
    return len(get_dir_content(dir)) == 0


def dir_to_string(dir: tuple):
    return get_dir_name(dir)


def make_file(name: str):
    return name, None


def get_file_name(file: tuple):
    return file[0]


def is_dir(node: tuple):
    return node[1] is not None


def file_to_string(file: tuple):
    return get_file_name(file)
