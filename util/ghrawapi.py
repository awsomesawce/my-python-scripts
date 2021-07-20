#!/usr/bin/env python
"""ghrawapi.py: Tool for interacting with raw github urls"""

import sys
import os
import json

import requests

stdout = sys.stdout
stderr = sys.stderr
request = requests.request
baseurl = "https://raw.githubusercontent.com"
user = "awsomesawce"
repo = "my-dotfiles"
branch = "master"
filename = ".editorconfig"
fullurl = f"{baseurl}/{user}/{repo}/{branch}/{filename}"

template_url = "https://raw.githubusercontent.com/awsomesawce/my-dotfiles/master/.editorconfig"

print(f"Attempting to download file from {fullurl}.  Please hold...")

#newreq = request('GET', "https://httpbin.org/get")
reqTwo = request('GET', template_url)
print(reqTwo)
#print(newreq.__repr__())
#print(requests.request.__doc__)

