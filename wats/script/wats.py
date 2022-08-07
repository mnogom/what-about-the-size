#!/usr/bin/env python3

from wats.cli import parse_args
from wats.builder import build_tree, sort_tree
from wats.renders import pick_render


def main():
    path, style, ignore_dirs = parse_args()
    tree = build_tree(path, ignore_dirs)
    tree = sort_tree(tree)
    render = pick_render(style)
    render(tree, path)


if __name__ == "__main__":
    main()
