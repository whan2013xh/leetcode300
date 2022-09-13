# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-06-30
    FileName   : peakIndexInMountainArray.py
    Author     : Honghe
    Descreption: 剑指 Offer II 069. 山峰数组的顶部
"""
from typing import List

class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        if len(arr)==3:
            return arr[1]
        left =0
        right = len(arr)-1

        while left<right:
            mid = (right-left)//2+left
            if left==mid:
                break
            if arr[mid]>arr[mid-1]:
                left = mid
            else:
                right = mid
        return left

if __name__ == '__main__':
    sol = Solution()
    arr = [1,5,10,2]
    print(sol.peakIndexInMountainArray(arr))



