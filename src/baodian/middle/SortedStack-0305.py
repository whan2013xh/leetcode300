# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-08-29
    FileName   : SortedStack-0305.py
    Author     : Honghe
    Descreption: 
"""

class SortedStack:

    def __init__(self):
        self.stack = []
        self.tmp_stack = []


    def push(self, val: int) -> None:
        while self.stack and self.stack[-1]<val:
            self.tmp_stack.append(self.stack.pop())
        self.stack.append(val)
        while self.tmp_stack:
            self.stack.append(self.tmp_stack.pop())

    def pop(self) -> None:
        if self.stack:
            self.stack.pop()


    def peek(self) -> int:
        return self.stack[-1] if self.stack else -1

    def isEmpty(self) -> bool:
        return len(self.stack)==0