"""Using internet_request.py"""
import sys
import os
import getopt

import internet_request

myreq = internet_request

myUrl = "https://httpbin.org"

d = myreq.convrequestedfile.__doc__

decoded = myreq.convrequestedfile(myUrl)

myreq.writetofile('hfile.html', decoded)
