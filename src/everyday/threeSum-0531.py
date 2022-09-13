# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-05-31
    FileName   : threeSum-0531.py
    Author     : Honghe
    Descreption: 15. 三数之和
"""

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums)<3:
            return []

        nums.sort()
        res = []
        pre = float("inf")

        for index,num in enumerate(nums):
            if num==pre:
                continue
            if num>0:
                break
            self.two_sum(nums,-num,index,res)
        return [list(i) for i in set(res)]


    def two_sum(self,nums, target,start,res):
        left = start+1
        right = len(nums)-1
        while left<right:
            if nums[left]+nums[right]>target:
                right-=1
            elif nums[left]+nums[right]<target:
                left+=1
            else:
                res.append((nums[start],nums[left],nums[right]))
                left+=1
                right-=1


if __name__ == '__main__':
    sol = Solution()
    nums = [-1, 0, 1, 2, -1, -4]
    print(sol.threeSum(nums))
