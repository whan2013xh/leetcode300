# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-08-08
    FileName   : MedianFinder-1720.py
    Author     : Honghe
    Descreption: 
"""
import heapq

class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.min_heapq = []
        self.max_heapq = []


    def addNum(self, num: int) -> None:
        """
        设计两个优先权队列/最小堆，通过将大于中位数的放在一个堆里，小于中位数的放在另一个堆里
        维持两个堆的元素个数不能相差超过1.
        :param num:
        :return:
        """
        if not self.min_heapq or num<-self.min_heapq[0]:
            heapq.heappush(self.min_heapq,-num)
            if len(self.min_heapq)>len(self.max_heapq)+1:
                tmp = heapq.heappop(self.min_heapq)
                heapq.heappush(self.max_heapq,-tmp)
        else:
            heapq.heappush(self.max_heapq,num)
            if len(self.max_heapq)>len(self.min_heapq)+1:
                tmp = heapq.heappop(self.max_heapq)
                heapq.heappush(self.min_heapq, -tmp)

    def findMedian(self) -> float:
        length1 = len(self.min_heapq)
        length2 = len(self.max_heapq)

        if length1==length2:
            return (-self.min_heapq[0]+self.max_heapq[0])/2
        elif length1>length2:
            return -self.min_heapq[0]
        else:
            return self.max_heapq[0]
        enumerate


if __name__ == '__main__':
    sol = MedianFinder()
    sol.addNum(1)
    sol.addNum(2)
    print(sol.findMedian())
    sol.addNum(3)
    print(sol.findMedian())

