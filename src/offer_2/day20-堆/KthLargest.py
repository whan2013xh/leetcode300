# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-06-27
    FileName   : KthLargest.py
    Author     : Honghe
    Descreption: 剑指 Offer II 059. 数据流的第 K 大数值
"""
from typing import List

class Max_heap:
    def __init__(self,data=None):
        """
        最大堆实现
        """
        self._data = [] if data is None else data
        self._count = len(self._data)
        self.heapfiy()

    def count(self):
        return self._count

    def _shift_up(self, index):
        parent = (index-1)>>1
        while index>0 and self._data[parent]<self._data[index]:
            self._data[index],self._data[parent]=self._data[parent],self._data[index]
            index = parent
            parent = (index - 1) >> 1

    def _shiht_down(self,index,end=None):
        child = (index<<1)+1
        end_index =self._count if end is None else end
        while child<self._count:
            if child >= end_index:
                break
            if child+1<end_index and self._data[child]<self._data[child+1]:
                child+=1
            if self._data[child]<=self._data[index]:
                break
            self._data[index],self._data[child] = self._data[child],self._data[index]
            index = child
            child = (index<<1)+1

    def get_data(self,index):
        return self._data[index] if abs(index)<self._count else None

    def pop(self):
        if not self._data:
            return None

        res = self._data[0]
        self._data[0] = self._data[-1]
        self._data.pop()
        self._count -= 1
        self._shiht_down(0)
        return res

    def add(self, value):
        self._data.append(value)
        self._shift_up(self._count)
        self._count += 1


    def heapfiy(self):
        for i in range(len(self._data)//2-1,-1,-1):
            self._shiht_down(i)

        for i in range(len(self._data)-1,0,-1):
            self._data[0],self._data[i] = self._data[i],self._data[0]
            self._shiht_down(0,i)


class Min_heap:
    def __init__(self,data=None,size=None):
        """
        最小堆实现,限制堆的大小
        """
        self._data = []
        self.total_data = data
        self.size = size
        self._count = 0
        self.heapfiy()

    def count(self):
        return self._count

    def _shift_up(self, index):
        parent = (index-1)>>1
        while index>0 and self._data[parent]>self._data[index]:
            self._data[index],self._data[parent]=self._data[parent],self._data[index]
            index = parent
            parent = (index - 1) >> 1

    def _shift_down(self,index,end=None):
        child = (index<<1)+1
        end_index =self._count if end is None else end
        while child<self._count:
            if child >= end_index:
                break
            if child+1<end_index and self._data[child]>self._data[child+1]:
                child+=1
            if self._data[child]>=self._data[index]:
                break
            self._data[index],self._data[child] = self._data[child],self._data[index]
            index = child
            child = (index<<1)+1

    def get_data(self,index):
        return self._data[index] if abs(index)<self._count else None

    def pop(self):
        if not self._data:
            return None

        res = self._data[0]
        self._data[0] = self._data[-1]
        self._data.pop()
        self._count -= 1
        self._shift_down(0)
        return res

    def add(self, value):
        if self._count==self.size:
            if value>self._data[0]:
                self._data[0] = value
                self._shift_down(0)
            return
        self._data.append(value)
        self._shift_up(self._count)
        self._count += 1


    def heapfiy(self):
        for num in self.total_data:
            self.add(num)


class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.heap = Min_heap(nums,k)
        self.target = k


    def add(self, val: int) -> int:
        self.heap.add(val)
        return self.heap.get_data(0)


if __name__ == '__main__':
    k=3
    nums = [4, 5, 8, 2]
    sol = KthLargest(k,nums)
    print(sol.add(3))
    print(sol.add(5))
    print(sol.add(10))