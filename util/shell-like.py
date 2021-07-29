#!python
"""shell-like python shortcuts"""

import os, sys
from base64 import b64encode

def ls(d=os.getcwd()) -> list:
    return os.listdir(d)

def b64str(s: str) -> bytes:
    return b64encode(s.encode())

print(b64str("yoyo"))
