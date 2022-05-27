# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-05-17
    FileName   : findMaxLength.py
    Author     : Honghe
    Descreption: 剑指 Offer II 011. 0 和 1 个数相同的子数组
"""


class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count_list = {}
        max_length = 0
        res = 0
        for index,num in enumerate(nums):
            tmp = 1 if num==1 else -1
            if not count_list:
                res = tmp
            else:
                res += tmp
            if res==0:
                max_length = max(max_length, index+1)
            else:
                if count_list.get(res) is not None:
                    max_length = max(max_length,index-count_list.get(res))
            count_list[res] = count_list.get(res,index)
        return max_length

if __name__ == '__main__':
    sol = Solution()
    nums = [0,0,1]
    print(sol.findMaxLength(nums))

