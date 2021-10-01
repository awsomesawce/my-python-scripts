#!/usr/bin/env python

import os
import sys


def add_to_set(l: list, s: set):
    for item in l:
        return s.add(item)


print("hello")
myset = set(["one", "two", "three"])
go_in_set = ["five", "six", "seven"]
add_to_set(go_in_set, myset)
myset_copy = myset.copy()
print(myset_copy)
