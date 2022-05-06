# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-04-24
    FileName   : numDecodings.py
    Author     : Honghe
    Descreption: 91. 解码方法
"""

class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        dp = [0]*len(s)
        for i in range(len(s)):
            num = int(s[i])
            if i==0:
                if num==0:
                    return 0
                dp[i]=1
            elif i==1:
                if int(s[:2])>26:
                    if num==0:
                        return 0
                    dp[i]=1
                    continue
                dp[i] = 2 if num!=0 else 1
            else:
                if int(s[i-1])==0:
                    if num==0:
                        return 0
                    dp[i] = dp[i-1]
                else:
                    if int(s[i-1:i+1])<=26:
                        if num!=0:
                            dp[i]= dp[i-1]+dp[i-2]
                        else:
                            dp[i] = dp[i-2]
                    else:
                        if num!=0:
                            dp[i] = dp[i-1]
                        else:
                            return 0
        return dp[-1]

    def numDecodings2(self, s: str) -> int:
        n = len(s)
        f = [1] + [0] * n
        for i in range(1,n):
            if s[i-1] != '0':
                f[i] += f[i - 1]
            if i > 1 and s[i - 2] != '0' and int(s[i - 2:i]) <= 26:
                f[i] += f[i - 2]
        return f[n]




if __name__ == '__main__':
    sol = Solution()
    s = "27"
    print(sol.numDecodings2(s))


