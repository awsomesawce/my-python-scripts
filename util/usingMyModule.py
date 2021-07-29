"""
====================
Using Module Imports
====================

Using internet_request.py as a module import

This is a demonstration of package resolution in Python.

It seems to work pretty nicely, and python's integrated
documentation support is just such a nice thing to have.  It is nice that
it is built *into the language* instead of having to rely on some third-party tooling.


"""
import sys
import os
import getopt

import './internet_request.py' as ireq

myreq = ireq

myUrl = "https://httpbin.org"

d = myreq.convrequestedfile.__doc__

decoded = myreq.convrequestedfile(myUrl)

myreq.writetofile('hfile.html', decoded)
