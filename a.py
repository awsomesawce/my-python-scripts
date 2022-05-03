#!/usr/bin/env python
"""
System Information
==================

Get and parse all sorts of system information available to python.

"""
import os, sys
import platform, site
from pprint import pprint
from pathlib import Path, PurePath

def finalPath(path, name):
    if os.path.exists(path):
        finalDict = {
            "name": name,
            "path": PurePath(os.path.abspath(path)),
            "repr": repr(PurePath(os.path.abspath(path)))
            }
        return f"{finalDict['name']} = {finalDict['repr']}"

print(finalPath('.', 'name'))

miniconda3 = PurePath(os.path.expanduser("~/miniconda3"))
print(f"miniconda3 = {repr(miniconda3)}")


##
##mingw = Path("D:\\MSYS2\\mingw64\\lib\\python3.9\\Tools")
##msys = Path("D:\\MSYS2\\usr\\lib\\python3.9")
current_msys = Path("C:\\msys64")

##
onedrive = PurePath(os.path.expandvars("$OneDrive"))
print(f"onedrive: {repr(onedrive)}")

currentdir = Path(os.path.abspath("."))
print(f"currentdir: {repr(currentdir)}")
##
##
##x = [x for x in os.listdir(pyscripts)]
##
##pp(x)
# print(os.sep.join([mingw, msys]))
