#!/usr/bin/python3
import argparse
import os

from mamba.codegen import CodeGen
from mamba.lexer import Lexer
from mamba.parser import Parser


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
    action="version",
    help="Shows the mamba version",
    version=f"%(prog)s 2.0a",
)

args = vars(parser.parse_args())
name = args["file"].split("/")[-1].split(".")[0]

with open(args["file"]) as f:
    text_input = f.read()

lexer = Lexer().get_lexer()
tokens = lexer.lex(text_input)

codegen = CodeGen()

module = codegen.module
builder = codegen.builder
printf = codegen.printf

pg = Parser(module, builder, printf)
pg.parse()
parser = pg.get_parser()
parser.parse(tokens).eval()

codegen.create_ir()
codegen.save_ir("output.ll")
os.system("llc -filetype=obj output.ll && rm output.ll")
os.system(f"gcc output.o -o {name} && rm output.o")
