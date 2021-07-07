#!/usr/bin/env python
# Working with files in python

import sys
import os

# import shutil
# import zipfile
# import argparse
import sysconfig


def detectpyver():
    """This function detects the python version
    It only displays the version in major.minor format."""
    x = sysconfig.get_python_version()
    if x == "3.9":
        print("python version is 3.9")
    elif x == "3.8":
        print("python version is 3.8")
    elif x == "3.7":
        print("python version is 3.7")
    elif x == "3.6":
        print("python version is 3.6 and is depreciated")
    else:
        print("not sure what version it is", file=sys.stderr)

detectpyver()

def showpyvers():
    """
    This func also detects the python version, but by using the __contains__ method
    sys.version is just a class 'str'.
    """
    y = sys.version
    if y.__contains__('3.8'):
        print('python version contains 3.8')
    elif y.__contains__('3.9'):
        print('python version string contains 3.9')
    else:
        print('not sure what version')

showpyvers()
