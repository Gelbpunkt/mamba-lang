#!/usr/bin/python3
# -*- coding: utf-8 -*-

import mamba
import sys
import argparse


def str2bool(v):
    if v.lower() in ("yes", "true", "t", "y", "1"):
        return True
    elif v.lower() in ("no", "false", "f", "n", "0"):
        return False
    else:
        raise argparse.ArgumentTypeError("Boolean value expected.")


parser = argparse.ArgumentParser(description="The Mamba programming language")
parser.add_argument("file", help="The file to execute")
parser.add_argument(
    "-l",
    "--limited",
    type=str2bool,
    dest="limited",
    help="Start in limited mode",
    required=False,
    const=True,
    default=False,
    nargs="?",
)
parser.add_argument(
    "-v",
    "--verbose",
    type=str2bool,
    dest="verbose",
    help="Shows the AST",
    required=False,
    const=True,
    default=False,
    nargs="?",
)
parser.add_argument(
    "--version",
    dest="version",
    help="Shows the mamba version",
    required=False,
    const=True,
    default=False,
)


def main():
    args = vars(parser.parse_args())
    if args["version"]:
        print(mamba.__version__)
    with open(args["file"]) as f:
        mamba.execute(f.read(), limited=args["limited"], show_ast=args["verbose"])


if __name__ == "__main__":
    main()
