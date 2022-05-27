# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-05-09
    FileName   : threeSum.py
    Author     : Honghe
    Descreption: 剑指 Offer II 007. 数组中和为 0 的三个数
"""
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums or len(nums)<3:
            return []
        nums.sort()
        res = set()
        for index,num in enumerate(nums[:-2]):
            if num>0 or -num < nums[index + 1]:
                break
            left = index+1
            right = len(nums)-1
            while left<right:
                if nums[left]+nums[right]==-num:
                    res.add((num,nums[left],nums[right]))
                    left+=1
                    right-=1
                elif nums[left]+nums[right]>-num:
                    right-=1
                else:
                    left+=1
        return [list(tmp) for tmp in res]

if __name__ == '__main__':
    sol = Solution()
    nums = [0,0,0]
    print(sol.threeSum(nums))