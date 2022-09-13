# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-06-22
    FileName   : RecentCounter.py
    Author     : Honghe
    Descreption: 剑指 Offer II 042. 最近请求次数
"""
from collections import deque


class RecentCounter:

    def __init__(self):
        self.deque = deque()


    def ping(self, t: int) -> int:
        if len(self.deque)==0:
            self.deque.append(t)
            return len(self.deque)

        tmp = t-3000
        self.deque.append(t)
        for i in range(len(self.deque)):
            num = self.deque.popleft()
            if num>=tmp:
                self.deque.appendleft(num)
                break
        return len(self.deque)

if __name__ == '__main__':
    sol = RecentCounter()
    print(sol.ping(1))
    print(sol.ping(100))
    print(sol.ping(3001))
    print(sol.ping(4000))





