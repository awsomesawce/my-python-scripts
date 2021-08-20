#!/usr/bin/env python
"""
System Information
==================

Get and parse all sorts of system information available to python.

"""
import os, sys
import platform, sitea
from pprint import pprint
import pathlib

pa = pathlib.PurePath


##
mingw = "D:\\MSYS2\\mingw64\\lib\\python3.9\\Tools"
msys = "D:\\MSYS2\\usr\\lib\\python3.9"
pyscripts = os.sep.join([mingw, "scripts"])
print(pyscripts)
##
##onedrive = "D:\\Carl\\OneDrive"
##
##
##x = [x for x in os.listdir(pyscripts)]
##
##pp(x)
# print(os.sep.join([mingw, msys]))
