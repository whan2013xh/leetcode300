# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-06-28
    FileName   : topKFrequent.py
    Author     : Honghe
    Descreption: 剑指 Offer II 060. 出现频率最高的 k 个数字
"""
from typing import List
from collections import OrderedDict,Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_count = Counter(nums)
        sorted_num = OrderedDict(sorted(num_count.items(),key=lambda t:t[1],reverse=True))
        res = []
        i=0
        for key,value in sorted_num.items():
            if i==k:
                return res
            res.append(key)
            i+=1
        return res


if __name__ == '__main__':
    nums = [1]
    sol = Solution()
    k=1
    print(sol.topKFrequent(nums,k))

