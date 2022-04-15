# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-04-08
    FileName   : threeSum.py
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
        # 1、排序
        nums.sort()
        # 2
        res = set()
        for index,num in enumerate(nums):
            target = -num
            if index<len(nums)-1 and target<nums[index+1]:
                break
            self.two_sum(nums,target,res,index)
        return [list(tmp) for tmp in res]

    def two_sum(self, nums,target,res,start):
        #
        left = start+1
        right = len(nums)-1
        while left<right:
            if nums[left]+nums[right]==target:
                res.add((nums[start],nums[left],nums[right]))
                left += 1
                right -= 1
            elif nums[left]+nums[right]>target:
                right -= 1
            else:
                left += 1
        return

if __name__ == '__main__':
    sol = Solution()
    nums = [-1]
    print(sol.threeSum(nums))

