# coding: utf-8
"""Working with namedtuples and json serialization
"""

import json as stdlib_json
import ujson as json # ujson is json as a c extension
import os
import sys

# Need most typings
from typing import (
    NamedTuple,
    List,
    Any,
    AnyStr,
    Union,
    Sequence,
    MutableSequence,
    Dict,
    MutableMapping
)

__all__ = ['JSONTuple2']

def loadjson(filename: Union[str, os.PathLike]) -> Dict[str, Any]:
    with open(filename) as f:
        return json.load(f)
    return False

class JSONTuple2(NamedTuple):
    """Proof of concept"""
    val1: str
    val2: int
    val3: Sequence[str]
    def printasjson(self) -> str:
        """Print as json string"""
        return json.dumps(self._asdict())
    def printannotations_json(self) -> str:
        """Print annotations as json string"""
        try:
            return json.dumps(self.__annotations__)
        except TypeError:
            return json.dumps(repr(self.__annotations__))
    @staticmethod
    def readfromjson(filename: Union[str,os.PathLike]) -> Dict[str,Any]:
        with open(filename) as file:
            return json.load(file)
        return False
    @classmethod
    def readfromjson2(cls, filename: Union[str,os.PathLike]) -> Any:
        """Doint it this way will not type-check at runtime
        If this works I will be soooo happy
        """
        result = loadjson(filename)
        return cls(*result.values())
        
        
