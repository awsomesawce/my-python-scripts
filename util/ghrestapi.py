#!/usr/bin/env python
"""GithubApiTest
Takes a url, requests it's content, prints it's content to stdout
Optionally prints to a file"""

import os, sys
import pathlib
import argparse
import json
from pprint import pprint

from requests import request
req = request

parser = argparse.ArgumentParser(description='Optionally write to file')
pprint(parser)
urls = ["https://api.github.com/repos", "https://httpbin.org/get"]
baseurl = urls[0]
for url in urls:
    print(url)

urlsdict = {
    "base": "https://api.github.com/repos",
    "second": "https://httpbin.org/get"
    }
pprint(urlsdict)

def getghapi(user, repo):
    """Returns a bytes-like object of the contents of the url
    This finally works.  Please do not mess it up by adding type annotations.
    
    """
    if (user == "awsomesawce"):
        response = req('Get', f"{baseurl}/awsomesawce/{repo}")
        print("You picked awsomesawce, good on ya :)")
        return response.content
    else:
        response = req('Get', f"{baseurl}/{user}/{repo}")
        return response

def outputtofile(s, filename):
    """Outputs a string (s) to file (filename)
    NOTIMPLEMENTED
    NOT TESTED"""
    with open(filename, 'w') as f:
        f.write(s)
        f.close()
        print("done")

##def parsejson(myjson) -> str:
##    """Supposed to parse the json to look pretty"""
##    return json.loads(myjson)

x = getghapi("awsomesawce", "my-python-scripts")
y = json.loads(x)
pprint(y)

