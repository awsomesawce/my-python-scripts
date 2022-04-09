# coding: utf-8
import os, sys, json, ujson, yarl
from typing import NamedTuple, OrderedDict, NewType, NoReturn, Any, List, Dict, Tuple, Text, MutableSequence, Sequence, AnyStr
from objectdict import ObjectDict # ObjectDict not needed in this case.


class Code_Points(NamedTuple):
    orig_string: str
    code_points: List[int]
    

d = Code_Points("string", [ord(c) for c in "string"])
    

def get_code_points(s: str):
    d = {"orig_str": s,
         "code_points": [ord(c) for c in s]}
    return d


cp = get_code_points("string")
arr = list(cp.values())
print(Code_Points(*arr))
cp_two = Code_Points(*[*get_code_points("str").values()])
print(json.dumps(cp_two._asdict()))
# get_ipython().run_line_magic('pinfo', '%save')
