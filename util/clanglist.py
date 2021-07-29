"""
===================================
Get a list of files in /clang64/bin
===================================

Uses function annotations too :)

:author: Carl C

:todo: Use os.walk or some other method to get file attributes and
print to stdout.
"""

__author__ = "Carl C."
__name__ = "clanglist"

import os, sys
from shelllike import ls, b64str

basedir = 'D:/MSYS2'
fulldir = f"{basedir}/clang64/bin"



def getlist(d=None):
    """
    Simply returns a list filled with dir entries
    """
    return os.listdir(d)

# Initialize list
mylist = ls(fulldir)

def printbyline(var: list) -> str:
    """Prints each item separated by newline
    There must be a better way!"""
    if type(var) == list:
        for item in var:
            print(item)

# This prints the list one by one in the console
printbyline(mylist)


