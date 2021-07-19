# -*- coding: utf-8 -*-
"""
    CreatedDate: 2021-07-15
    FileName   : merge.py
    Author     : Honghe
    Descreption: 56. 合并区间
"""

class Solution(object):
    def merge(self, intervals):
        """
        排序法：先排序后再合并
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        if len(intervals)<=1:
            return intervals

        result = []
        intervals.sort(key = lambda x:x[0])
        for interval in intervals:
            if len(result)==0 or interval[0]>result[-1][1]:
                result.append(interval)
            else:
                result[-1][1] = max(result[-1][1], interval[1])
        return result


if __name__ == '__main__':
    intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
    sol = Solution()
    res = sol.merge(intervals)
    print(res)

