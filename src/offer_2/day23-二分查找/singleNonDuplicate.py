# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-07-01
    FileName   : singleNonDuplicate.py
    Author     : Honghe
    Descreption: 剑指 Offer II 070. 排序数组中只出现一次的数字
"""
from typing import List

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        return self.find(nums,left,right)



    def find(self,nums,left,right):
        if left>right:
            return -1

        if left<right:
            mid = (right-left)//2+left
            if 0<mid<len(nums)-1 and nums[mid-1]<nums[mid]<nums[mid+1]:
                return nums[mid]
            elif mid<len(nums)-1 and nums[mid]==nums[mid+1]:
                res = self.find(nums,left,mid-1)
                if res!=-1:
                    return res
                right_res = self.find(nums,mid+2,right)
                return right_res
            elif mid>0 and nums[mid]==nums[mid-1]:
                res = self.find(nums, left, mid - 2)
                if res != -1:
                    return res
                right_res = self.find(nums, mid + 1, right)
                return right_res
        return nums[left]

if __name__ == '__main__':
    sol = Solution()
    nums = [3,3,7,7,10,11,11]
    print(sol.singleNonDuplicate(nums))
