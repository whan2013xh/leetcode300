# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-07-28
    FileName   : arrayRankTransform-0728.py
    Author     : Honghe
    Descreption: 
"""
from typing import List
from collections import defaultdict

class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        if not arr:
            return []
        arr_dic = defaultdict(list)
        for index,num in enumerate(arr):
            arr_dic[num].append(index)
        arr_dic = sorted(arr_dic.items(),key=lambda x:x[0])
        res = [1]*len(arr)
        count = 1
        for value,index in arr_dic:
            for i in index:
                res[i] = count
            count+=1
        return res


if __name__ == '__main__':
    sol = Solution()
    arr = [37,12,28,9,100,56,80,5,12]
    print(sol.arrayRankTransform(arr))