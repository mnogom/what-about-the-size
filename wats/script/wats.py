#!/usr/bin/env python3

from wats.cli import parse_args
from wats.builder import build_tree, sort_tree
from wats.renders.tree_render import render


def main():
    path, limit_from, ignore_dirs = parse_args()
    tree = build_tree(path, ignore_dirs)
    tree = sort_tree(tree)
    print(path)
    result = render(tree, path)

    print(result)


if __name__ == "__main__":
    main()
