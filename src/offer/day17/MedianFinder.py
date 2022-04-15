# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-04-07
    FileName   : MedianFinder.py
    Author     : Honghe
    Descreption: 剑指 Offer 41. 数据流中的中位数
"""
class MedianFinder(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.nums = []

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        if not self.nums:
            self.nums.append(num)
            return
        if len(self.nums)==1:
            index = 0 if self.nums[0]>num else 1
            self.nums.insert(index,num)
            return
        left = 0
        right = len(self.nums)-1
        while left<=right:
            middle = (right-left)//2+left
            if self.nums[middle]>=num:
                if (middle-1>=left and self.nums[middle-1]<=num) or middle==left:
                    index = middle
                    self.nums.insert(index, num)
                    return
                else:
                    right = middle-1
            else:
                if (middle+1<=right and self.nums[middle+1]>=num) or middle==right:
                    index = middle+1
                    self.nums.insert(index, num)
                    return
                else:
                    left = middle+1
        self.nums.insert(left,num)
        return


    def findMedian(self):
        """
        :rtype: float
        """
        if not self.nums:
            return None
        if len(self.nums)==1:
            return self.nums[0]
        flag = len(self.nums)%2==0
        middle = len(self.nums) // 2
        if flag:
            return (self.nums[middle]+self.nums[middle-1])/2
        return self.nums[middle]

if __name__ == '__main__':
    sol = MedianFinder()
    # sol.addNum(1)
    sol.addNum(6)
    print(sol.findMedian())
    sol.addNum(10)
    print(sol.findMedian())
    sol.addNum(2)
    print(sol.findMedian())
    sol.addNum(6)
    print(sol.findMedian())
    sol.addNum(5)
    print(sol.findMedian())
    sol.addNum(0)
    print(sol.findMedian())
    sol.addNum(6)
    print(sol.findMedian())
    sol.addNum(3)
    print(sol.findMedian())
    sol.addNum(1)
    print(sol.findMedian())
    sol.addNum(0)
    print(sol.findMedian())
    sol.addNum(0)
    print(sol.findMedian())