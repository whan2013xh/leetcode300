# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-06-16
    FileName   : findMinDifference.py
    Author     : Honghe
    Descreption: 剑指 Offer II 035. 最小时间差
"""


class Solution(object):
    def findMinDifference(self, timePoints):
        """
        :type timePoints: List[str]
        :rtype: int
        """
        if len(timePoints) > 24 * 60:
            return 0
        mins = sorted(int(t[:2]) * 60 + int(t[3:]) for t in timePoints)
        mins.append(mins[0] + 24 * 60)
        return min(mins[i] - mins[i - 1] for i in range(1, len(mins)))


