# Used to system info and other data
# Variables are handled in varproc.py

import os, sys

ARGV = sys.argv
ARGC = len(ARGV)

INC = {
    "fn", "method",
    "for", "loop", "while",
    "if", "if-then",
    "thread",
    "ismain", "isntmain",
    "expect", "expect-then",
    "body"
}

DEC = {
    "end"
}

CHARS = {
    "\\\\":"\\[escape]",
    "\\n":"\n",
    "\\t":"\t",
    "\\s":" ",
    "\\v":"\v",
    "\\f":"\f",
    "\\r":"\r",
    "\\a":"\a",
    "\\0":"\0",
    "\\[win_nl]":"\r\n",
    "\\[posix_nl]":"\n",
    "\\[null]":"\0",
    "\\[alert]":"\a",
    "\\[escape]":"\\",
}

BINDIR = os.path.dirname(ARGV[0])
LIBDIR = os.path.join(BINDIR, "lib")
CORE_DIR = os.path.join(BINDIR, "lib", "core")

PYTHON_VER = sys.version

if __name__ == "__main__":
    for name, value in globals().copy().items():
        print(f"{name} = {value!r}")