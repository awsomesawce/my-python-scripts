#!python
"""shell-like python shortcuts"""

import os, sys
from base64 import b64encode

def ls(d=os.getcwd()) -> list:
    """Returns a list of files in a directory
    cwd is default"""
    return os.listdir(d)

def b64str(s: str) -> bytes:
    """Prints out a b64 encoded string"""
    return b64encode(s.encode())

#print(b64str("yoyo"))
