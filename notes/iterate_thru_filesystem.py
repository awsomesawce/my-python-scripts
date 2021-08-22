#!/usr/bin/env python
"""Using python to iterate thru file system objects"""

import os
import sys
from pathlib import Path
from pprint import pprint

def ls(d=os.getcwd()):
	d_abs = os.path.abspath(d)
	if os.path.exists(d):
		print(f"Here is the contents of {d_abs}:")
		return pprint(os.listdir(d_abs))
	else:
		raise Exception("{d} path does not exist")

def funWithPaths(path):
    return Path(path)

ls('..')

file_path = funWithPaths("./Conda.md")

print(file_path.absolute())

##def changeSysPath(p, options):
##    return [p, options]
##
##print(changeSysPath("one", "two"))
