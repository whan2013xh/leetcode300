# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-08-31
    FileName   : isMatch-0831.py
    Author     : Honghe
    Descreption: 10. 正则表达式匹配
"""

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        """
        动态规划，从前往后
        :param s:
        :param p:
        :return:
        """
        m = len(s)
        n = len(p)
        dp = [[False]*(n+1) for _ in range(m+1)]
        # 初始化边界
        dp[0][0]=True  #都为空时，肯定可以匹配
        for i in range(1,n+1):
            if p[i-1]=="*":
                if i>=2:
                    dp[0][i]=dp[0][i-2]
                else:
                    dp[0][i] = True

        for i in range(1,m+1):
            for j in range(1,n+1):
                if s[i-1]==p[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    if p[j-1]==".":
                        dp[i][j] = dp[i - 1][j - 1]
                    elif p[j-1]=="*":
                        dp[i][j] = dp[i][j-2]|dp[i][j-1]
                        if j>=2 and (p[j-2]==s[i-1] or p[j-2]=="."):
                            dp[i][j] |= dp[i-1][j]
        return dp[m][n]

if __name__ == '__main__':
    sol = Solution()
    s = "aaa"
    p = "ab*a"
    print(sol.isMatch(s,p))
