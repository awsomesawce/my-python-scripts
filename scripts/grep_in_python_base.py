#!/usr/bin/env python3

import os
import sys
import argparse
import re

with open(sys.argv[2],"r") as file:
    for line in file:
        if re.search(sys.argv[1], line):
            print(line)

