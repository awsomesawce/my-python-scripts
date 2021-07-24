#!/usr/bin/env python
# Read a file

__name__ = 'go_to_home.py'
__author__ = 'Carl C.'
__doc__ = """This program goes to the USERPROFILE directory
and is _supposed_ to get the ps1 files in the current directory
_after_ it changes to home.
I think the reason is that the two separate functions are in different
scopes."""

import os
import sys
from glob import glob
#import json
#import re

if os.name == 'nt':
    print("This is windows nt platform.\nUse \"\\\\\" as path separator.")
    print(f"""
You can actually use os.sep to get the pathname separators like so:
{os.sep}: it prints as one backslash but is actually two.
""")
else:
    print("This is not windows, so most likely we will be using " +
          os.sep + " as path seperators")



def changetohome():
    """
    When this function is done it will detect what dir your in
    and if your not in the USERPROFILE dir it will
    change to it
    """
    cdir = os.getcwd()
    homedir = os.getenv('USERPROFILE')
    if cdir != homedir:
        print(f"{cdir} is not equal to {homedir}")
        print("Going to homedir")
        os.chdir(homedir)
        newdir = os.getcwd()
        print(f"Now in {newdir}")
        print(getps1files(homedir)) # Why does this work?
    else:
        print(f"Already in {homedir}")


def getps1files(dirent=os.getcwd()):
    """This function gets all ps1 files in directory."""
    return glob(f'{dirent}\\*.ps1')

changetohome()
print(getps1files())
##binlist = getps1files(os.environ.get('USERPROFILE')+'\\bin')
##print(binlist)
