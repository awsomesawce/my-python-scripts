#!/usr/bin/env python
"""Learning python classes"""

class C():
    """This is a class"""
    def __init__(self):
        """ This is the init"""
        self.self = self # I don't know what this means.

    def add(x, y):
        """This adds two numbers"""
        return x + y


ans = C.add(1, 2)
print(ans)
