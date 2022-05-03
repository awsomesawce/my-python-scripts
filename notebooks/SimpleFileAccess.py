"""Discovery of new packages"""

import os, sys, sysconfig, site, platform
import json5, json
import collections
import typing
from types import SimpleNamespace
from collections import deque, defaultdict, namedtuple, OrderedDict
import toml
import glob, asyncio
import json5
import pip

favorites = {
    "what_is_happening": "I am using binder",
    "modules": collections.OrderedDict({
        "globbing": ["os", "glob", "fnmatch"],
        "encodings": ["base64", "binascii"]
    }),
    "files": {
        "json": []
    }
}

print(glob.iglob("../*.json"))

print(favorites)
