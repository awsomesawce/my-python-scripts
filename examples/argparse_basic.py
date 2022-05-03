#!/usr/bin/env python
"""Argparse basic example
Why the fuck is vscode taking so long"""

import argparse
import black
import os, sys

EPILOG = """
Made by Carl C.
This is hard
Gotta look up docs for this one"""

argparse.Action

parser = argparse.ArgumentParser("new", """usage
    This is the usage
    """, "desc", EPILOG, add_help=True)

parser.add_argument('-f', action='hey', version='0.0.1')

if __name__ == '__main__':
    parser.parse_args()
    print(parser)
