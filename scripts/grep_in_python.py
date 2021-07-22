#!/usr/bin/env python3
"""Simple grep using python code
Argparse import is not needed in this case
"""

import os
import sys
import argparse
import re

with open(sys.argv[2],"r") as file:
    for line in file:
        if re.search(sys.argv[1], line):
            print(line)

