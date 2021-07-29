#!python
# Network and internet requests
"""An attempt to use python stdlib to request a file on the web
using urllib.request.urlopen() and write the data to a file.

Try using Pathlib for interacting with filesystem.
"""

__author__ = "Carl C"
__license__ = """MIT"""

import os

# import sys
# from pprint import pprint
# import requests
import urllib.request as req


def dlfile(urlname=None):
    """
    Download file from url.

    :param urlname: string of the url in question

    :returns: a urlopen object

    Example:
    downloaded = dlfile("https://api.github.com")

    """
    rq = req.urlopen(urlname)
    if rq.code == 200:
        return rq
    else:
        print("there was a problem")


def convrequestedfile(urlname=None):
    """Convert requested file back to string like object
    :example: decodedrequest = convrequestedfile('https://httpbin.org/get')

    :returns: a string that is already decoded
    See ``writetofile`` for a function to write the string to a file
    """
    result = req.urlopen(urlname)
    if result.code == 200:
        readed = result.read()  # TODO: Find a better word than "readed"
        decoded = readed.decode()
        return decoded
    else:
        raise BaseException(r"There was a problem with the request")


def writetofile(filename, string_to_write):
    """Takes a string and writes to a filename
    TODO: Figure out why os.path.exists is not WORKING

    Example: writetofile("myfile.html", htmlbuffer)
    """
    if os.path.exists(filename):
        return f"Error: {filename} exists already"
    else:
        with open(filename, "w", encoding="utf8") as fd:
            fd.write(string_to_write)
            fd.close()


__example__ = """
Check docstrings for examples
"""

__comments__ = "Now I just need to find the correct stdlib module that allows writing to the filesystem."
