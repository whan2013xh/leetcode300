# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-08-26
    FileName   : StackOfPlates-0303.py
    Author     : Honghe
    Descreption: 
"""


class StackOfPlates:

    def __init__(self, cap: int):
        self.cap = cap
        self.stacks = []


    def push(self, val: int) -> None:
        if self.cap<=0:
            return

        if not self.stacks:
            self.stacks.append([val])
        else:
            cur = self.stacks[-1]
            if len(cur)==self.cap:
                self.stacks.append([val])
            else:
                cur.append(val)


    def pop(self) -> int:
        if self.cap<=0:
            return -1
        if not self.stacks:
            return -1
        res = self.stacks[-1].pop()
        if len(self.stacks[-1])==0:
            self.stacks.pop()
        return res


    def popAt(self, index: int) -> int:
        if self.cap<=0:
            return -1
        if index>=len(self.stacks) or index<0:
            return -1
        cur = self.stacks[index]
        res = cur.pop()
        if not cur:
            self.stacks.pop(index)
        return res


if __name__ == '__main__':
    sol = StackOfPlates(1)
    sol.push(1)
    sol.push(2)
    sol.push(3)
    print(sol.popAt(0))
    print(sol.popAt(0))
    print(sol.popAt(0))
