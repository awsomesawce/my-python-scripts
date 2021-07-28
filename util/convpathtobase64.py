#!/usr/bin/env python
# Base64 encode a path-like object
"""With as little code as possible, encode a string object into
bytes, then into base64.
Optionally create shell script from this (python -m myscript mystring)"""

import os
import sys
import pathlib
import base64

encode = base64.standard_b64encode

def getbase64str(mystr: bytes) -> bytes:
    """Convert string into bytes into base64
    if the type is a bytes-like object, require no further bytes() method"""
    if (type(mystr) == type(b'test')):
        newstr = encode(mystr)
        return newstr
    else:
        newstr = encode(bytes(mystr, 'utf8'))
        return newstr

def printthestr(mystr):
    "Wrapper around getbase64str"
    return print(getbase64str(mystr))

teststr = b"This is a test str"
printthestr(teststr)
z = sys.argv.copy()
print(f"{z} is new str.argv")
print(getbase64str(f"{os.getcwd()}")) # Gets current working directory as base64
print(getbase64str("my string"))
#print(myNewStr)
##
##
##my_cwd = os.getcwd()
##testp = pathlib.Path
##mypath = testp.cwd()
##myuri = mypath.as_uri()
##bytes(myuri, 'utf8')
#
# b'file:///C:/Users/Carl/gitstuff/my-python-scripts'
##mybytes = bytes(myuri, 'utf8')
##print(mybytes)
##mybase = base64.standard_b64encode(mybytes)
##print(mybase)

