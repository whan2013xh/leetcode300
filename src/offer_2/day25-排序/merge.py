# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-07-04
    FileName   : merge.py
    Author     : Honghe
    Descreption: 剑指 Offer II 074. 合并区间
"""
from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])
        start,end = intervals[0]
        res = []
        for interval in intervals[1:]:
            if interval[0]>end:
                res.append([start,end])
                start, end = interval
            else:
                end = max(end,interval[1])
        res.append([start,end])
        return res


if __name__ == '__main__':
    sol = Solution()
    intervals = [[1,4],[2,3]]
    print(sol.merge(intervals))
