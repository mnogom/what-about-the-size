import os

import argparse


def parse_args():
    parser = argparse.ArgumentParser(description="Get file sizes")
    parser.add_argument("-p", "--path",
                        default=os.getcwd(),
                        required=False)
    parser.add_argument("-s", "--style",
                        default="tree")
    parser.add_argument("-i", "--ignore-dirs",
                        nargs="*",
                        default=[],
                        required=False)
    args = parser.parse_args()
    ignore_dirs = [os.path.join(args.path,
                                ignore_dir) for ignore_dir in args.ignore_dirs]
    return args.path, args.style, ignore_dirs
