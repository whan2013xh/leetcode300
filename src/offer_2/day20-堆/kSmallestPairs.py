# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-06-28
    FileName   : kSmallestPairs.py
    Author     : Honghe
    Descreption: 剑指 Offer II 061. 和最小的 k 个数对
"""
from typing import List
from collections import OrderedDict,defaultdict

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        num_sum = defaultdict(list)
        for num1 in nums1:
            for num2 in nums2:
                num_sum[num1+num2].append([num1,num2])

        sorted_nums = OrderedDict(sorted(num_sum.items(),key=lambda t:t[0]))
        res = []
        for key,value in sorted_nums.items():
            if k-len(res)>=len(value):
                res+=value
            elif 0<k-len(res)<len(value):
                res +=value[:k-len(res)]
            else:
                return res
        return res


if __name__ == '__main__':
    sol = Solution()
    nums1 = [1, 7, 11]
    nums2 = [2, 4, 6]
    k = 3
    print(sol.kSmallestPairs(nums1,nums2,k))


