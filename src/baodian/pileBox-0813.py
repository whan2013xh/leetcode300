# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-08-01
    FileName   : pileBox-0813.py
    Author     : Honghe
    Descreption: 面试题 08.13. 堆箱子https://leetcode.cn/problems/pile-box-lcci/
"""
from typing import List

class Solution:
    def pileBox(self, box: List[List[int]]) -> int:
        if not box:
            return 0

        box = set([tuple(box[i]) for i in range(len(box))])
        box = sorted(box, key=lambda x:x[-1])
        dp = [0] * len(box)
        dp[0]=box[0][-1]
        for i in range(1,len(box)):
            w,d,h = box[i]
            dp[i] = h
            for j in range(i-1,-1,-1):
                pre = box[j]
                if w>pre[0] and d>pre[1] and h>pre[-1]:
                    dp[i] = max(dp[i],dp[j]+h)
        return max(dp)

if __name__ == '__main__':
    sol = Solution()
    box = [[3, 1, 4], [10, 16, 15], [9, 10, 20], [8, 9, 8], [19, 7, 8], [10, 8, 2], [18, 16, 6], [8, 4, 9], [13, 1, 10], [18, 4, 6], [14, 8, 16], [13, 18, 2], [17, 10, 16], [4, 6, 6], [11, 17, 7], [1, 8, 7], [16, 10, 15], [18, 18, 4], [7, 2, 12], [1, 7, 3], [8, 5, 4], [15, 4, 9], [16, 7, 6], [12, 13, 20], [2, 4, 3], [12, 13, 20], [1, 2, 13], [16, 20, 11], [14, 4, 17], [16, 15, 8], [15, 18, 17], [4, 4, 8], [5, 18, 1], [16, 10, 10], [17, 19, 13], [18, 20, 13], [17, 5, 19], [5, 2, 17], [7, 13, 13], [9, 11, 12], [11, 10, 12], [10, 16, 5], [4, 3, 18], [18, 11, 18], [14, 14, 16], [18, 1, 14], [7, 5, 19], [10, 15, 11], [2, 11, 8], [6, 8, 17], [12, 1, 12], [8, 4, 17], [13, 14, 11], [17, 20, 11], [15, 10, 15], [7, 6, 19], [14, 13, 15], [11, 9, 12], [19, 14, 2], [14, 11, 8], [4, 2, 18], [12, 20, 15], [2, 12, 18], [16, 6, 9]]
    print(sol.pileBox(box))