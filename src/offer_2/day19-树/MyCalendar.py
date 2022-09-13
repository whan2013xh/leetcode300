# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-06-27
    FileName   : MyCalendar.py
    Author     : Honghe
    Descreption: 剑指 Offer II 058. 日程表
"""
from collections import deque

class Node_tree:
    def __init__(self,start,end, left=None,right=None):
        self.start = start
        self.end=end
        self.left = left
        self.right = right

    def insert(self, node,root):
        if node.end<root.start:
            if root.left:
                return self.insert(node,root.left)
            root.left = node
            return True
        elif node.start>root.end:
            if root.right:
                return self.insert(node,root.right)
            root.right = node
            return True
        return False

class MyCalendar:

    def __init__(self):
        self.start_time = deque()
        self.end_time = deque()


    def book(self, start: int, end: int) -> bool:
        if not self.start_time or start>self.end_time[-1]:
            self.start_time.append(start)
            self.end_time.append(end-1)
            return True
        elif end-1<self.start_time[0]:
            self.start_time.appendleft(start)
            self.end_time.appendleft(end - 1)
            return True

        start_index = self.find_index(end-1,self.start_time)

        if self.end_time[start_index-1]<start:
            self.start_time.insert(start_index,start)
            self.end_time.insert(start_index,end - 1)
            return True
        return False


    def find_index(self,num, num_list):
        left = 0
        right = len(num_list)
        index = (right-left)//2+left
        while left<right:
            if num_list[index]>num:
                right = index
            elif num_list[index]==num:
                return index+1
            else:
                left = index+1
            index = (right - left) // 2 + left
        return index


if __name__ == '__main__':
    sol = MyCalendar()
    print(sol.book(19,26))
    print(sol.book(3,10))
    print(sol.book(39,44))
    print(sol.book(35, 40))

    print(sol.book(3,12))
    print(sol.book(5, 13))
    print(sol.book(11, 17))
    print(sol.book(47, 50))
    print(sol.book(29,37))
    print(sol.book(26, 34))
    # print(sol.book(18, 27))

