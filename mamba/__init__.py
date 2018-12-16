import time
import mamba.parser as p
import mamba.ast
import mamba.environment
import mamba.exceptions
import pprint
import sys
import resource
import signal

__version__ = "0.1.0"


def execute(
    source, show_ast: bool = False, disable_warnings: bool = True, limited: bool = False
):
    p.disable_warnings = disable_warnings

    if limited:

        def handler(num, frame):
            raise TimeoutError("The code execution took too long")

        resource.setrlimit(
            resource.RLIMIT_AS, (300000000, 300000000)
        )  # limit the memory usage, it's high because mamba uses a lot for parsing

        signal.signal(signal.SIGALRM, handler)
        signal.alarm(5)  # allow up to 5 seconds of execution

    try:
        res = p.get_parser().parse(source)
        environment.declare_env(mamba.ast.symbols, limited=limited)

        for node in res.children:
            node.eval()

        if show_ast:
            print("\n\n" + "=" * 80, " == Syntax tree ==")

            pp = pprint.PrettyPrinter()
            pp.pprint(res.children)
            pp.pprint(mamba.ast.symbols.table())
    except Exception as e:
        print(e.__class__.__name__ + ": " + str(e), file=sys.stderr)
        if not disable_warnings:
            raise e
