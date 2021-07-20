#!/usr/bin/env python
"""Os-Specific template/snippet"""

import os
import sys

if os.name == "win32":
    print("here are some windows-specific things")
    #homedir = os.getenv('USERPROFILE')
elif os.name == "posix":
    print("here are some posix-specific things")
    #homedir = os.getenv('HOME')
    #currentdir = os.getcwd()
else:
    # This is quite rare
    # Most OS's are either of the two.
    raise OSError('Not posix or win32')