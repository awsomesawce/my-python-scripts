"""Object Dict from tornado.util
Reduce contained code to it's absolute minimum and import what you need.
"""

from pprint import pprint
from typing import Dict, List, Any, AnyStr, NamedTuple, Tuple, Union, Sequence
import json
import os, sys

__all__ = [
    'ObjectDict'
]

class ObjectDict(Dict[str, Any]):
    """Makes a dictionary behave like an object, with attribute-style access.
    Analogous to how javascript objects work.
    From tornado.util
    """

    _version = "0.2"

    def __getattr__(self, name: str) -> Any:
        try:
            return self[name]
        except KeyError:
            raise AttributeError(name)

    def __setattr__(self, name: str, value: Any) -> None:
        self[name] = value

    def printmyjson(self):
        return json.dumps(self)

    @staticmethod
    def printjson(val):
        return json.dumps(val)

d = ObjectDict({"test": True})

def test():
    '''This will only execute if executed as a script'''
    d = ObjectDict()
    d.one = 1
    d.two = 2
    print(json.dumps(d))

if __name__ == "__main__":
    test()
