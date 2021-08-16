# -*- coding: utf-8 -*-
"""
    CreatedDate: 2021-08-16
    FileName   : nthUglyNumber.py
    Author     : Honghe
    Descreption: 264. 丑数 II
"""

class Solution(object):
    def nthUglyNumber(self, n):
        """
        动态规划法：其实dp[n] = min(dp[0~n-1]*[2,3,5])
        维护一个visited类似的记录在因子2，3，5都已经使用的次数
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        dp = [0] * n
        dp[0] = 1
        # 因子使用的次数
        p2 = p3 = p5 = 0
        for i in range(1, n):
            dp[i] = min(dp[p2] * 2, dp[p3] * 3, dp[p5] * 5)
            if dp[i] == dp[p2] * 2:
                p2 += 1
            if dp[i] == dp[p3] * 3:
                p3 += 1
            if dp[i] == dp[p5] * 5:
                p5 += 1
        return dp[-1]


if __name__ == '__main__':
    n = 10
    sol = Solution()
    print([2,3,5]*2)
    res = sol.nthUglyNumber(n)
    print(res)
