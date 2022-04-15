# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-04-14
    FileName   : minSubArrayLen.py
    Author     : Honghe
    Descreption: 209. 长度最小的子数组
"""
class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        res = float("inf")
        left = 0
        tmp = 0
        for right,num in enumerate(nums):
            tmp+=num
            while tmp>=target and left<=right:
                res = min(res, right - left + 1)
                tmp-=nums[left]
                left+=1

        return res if res!=float("inf") else 0

if __name__ == '__main__':
    sol = Solution()
    nums =[2,3,1,2,4,3]
    target =3
    print(sol.minSubArrayLen(target,nums))





