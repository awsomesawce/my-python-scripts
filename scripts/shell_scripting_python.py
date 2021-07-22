#!/usr/bin/env python
"Working with files in python"

__author__ = 'Carl C. <awsomesawce@outlook.com>'
__date__ = 'July-22-2021'

import sys
import os
import getopt

filename = sys.argv

def cli():
    """Command-line interface test.  Looks at sys.argv.
    Taken fron pydoc script in stdlib"""
    class BadUsage(Exception): pass
    try:
        newvar = None
        opts, args = getopt.getopt(sys.argv[1:], 'a:b:c')
        for opt, val in opts:
            if opt == '-a':
                newvar = "You picked a"
            if opt == '-b':
                newvar = "You picked b"
                return
            if opt == '-c':
                newvar = "You picked c"

            if not args: raise BadUsage

        print(f"newvar is {newvar}")
##        if os.path.exists(filename):
##            return "path exists"
##        else:
##            return "path does not exist"
    except (getopt.error, BadUsage):
        print(f"sys.argv is {sys.argv}")


if __name__ == '__main__':
    cli()
