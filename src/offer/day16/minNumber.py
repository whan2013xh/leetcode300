# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-04-07
    FileName   : minNumber.py
    Author     : Honghe
    Descreption: 剑指 Offer 45. 把数组排成最小的数
"""

class Solution(object):
    def minNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        for index,num in enumerate(nums):
            min_num = num
            for j in range(index+1,len(nums)):
                if int(str(min_num)+str(nums[j]))>int(str(nums[j])+str(min_num)):
                    min_num,nums[j]=nums[j],min_num
            nums[index] = min_num
        res = ""
        for i in nums:
            res += str(i)
        return res

if __name__ == '__main__':
    sol = Solution()
    nums=[121,12]
    print(sol.minNumber(nums))