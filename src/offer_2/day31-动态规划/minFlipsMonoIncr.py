# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-07-07
    FileName   : minFlipsMonoIncr.py
    Author     : Honghe
    Descreption: 
"""


class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        """
        动态规划
        :param s:
        :return:
        """
        dp = [[0]*2 for _ in range(len(s))]
        for i in range(len(s)):
            if i==0:
                if s[i]=="0":
                    dp[i][0]=0
                    dp[i][1]=1
                else:
                    dp[i][0] = 1
                    dp[i][1] = 0
            else:
                if s[i]=="0":
                    dp[i][0]=dp[i-1][0]
                    dp[i][1] = min(dp[i-1][1],dp[i-1][0])+1
                else:
                    dp[i][0] = dp[i - 1][0]+1
                    dp[i][1] = min(dp[i-1][0],dp[i-1][1])
        return min(dp[-1][:])

    def minFlipsMonoIncr2(self, s: str) -> int:
        zero = 0
        one = 0
        for i in range(len(s)):
            if s[i]=="0":
                zero = min(one,zero+1)
            else:
                one+=1
        return zero

if __name__ == '__main__':
    sol = Solution()
    s = "00110"
    print(sol.minFlipsMonoIncr2(s))