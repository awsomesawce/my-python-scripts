#!python
"""Argparse test"""

import argh
import os, sys
import sysconfig
from pprint import pprint
import shelllike

##envvars = os.environ.copy()
##
##parser = argparse.ArgumentParser(
##    description='Testing the argparse lib')
##parser.add_argument('sysconfig', metavar='TheString', type=str,
##                    help='help for the command')
##
##args = parser.parse_args()
##print(args.sysconfig)

print(sys.argv)


def iterArgv():
    for a in sys.argv:
        return a + "\n"


print(iterArgv())

##if sys.argv[1]: argone = sys.argv[1]
##if sys.argv[2]: argtwo = sys.argv[2]
args = sys.argv

# if args.count(1) > 0: raise Exception("too little args")
if args[1] == 1:
    print("You typed 1 as your first argument!")

##
##if argone and argtwo:
##    print(f"{argone} and {argtwo}")
