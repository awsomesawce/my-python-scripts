# coding: utf-8
from pathlib import Path, PurePath
import os, sys
import json
import gzip, zlib
from typing import List, Tuple, Sequence, Union
from dataclasses import dataclass, field, fields, asdict, astuple, InitVar
class UsingGzip:
    def __init__(self, file: str) -> None:
        self.file = file
    def __repr__(self):
        return f'UsingGzip(file={self.file})'
    def aspath(self):
        if Path:
            return Path(self.file)
        else:
            raise AssertionError("pathlib has not been imported yet")
    #
    @staticmethod
    def dumpgzip(filename):
        "Attempt to dump gzip-compressed data from a file to stdout"
        if Path(filename).exists():
            with Path(filename).open("rb") as f:
                content = f.read()
            return gzip.compress(content)
        else:
            raise AssertionError(f"filename at {filename} did not exist")
    #
    
@dataclass
class UsingGzDc:
    """This one actually works just fine!
Give this class a filename, and it will do whatever you want with it!
"""
    file: Union[str,os.PathLike]
    def create_path(self):
        return Path(self.file)
    def get_contents(self):
        with open(self.file, "rb") as f:
            contents = f.read()
        return contents
    def gzip_contents(self):
        return gzip.compress(self.get_contents())
