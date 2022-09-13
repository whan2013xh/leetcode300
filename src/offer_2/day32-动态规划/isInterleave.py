# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-07-11
    FileName   : isInterleave.py
    Author     : Honghe
    Descreption: 
"""


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        """
        递归法
        :param s1:
        :param s2:
        :param s3:
        :return:
        """
        if len(s1)+len(s2)!=len(s3):
            return False

        if not s1 and not s2 and not s3:
            return True

        if s1 and s2 and s3[-1]==s1[-1]==s2[-1]:
            return self.isInterleave(s1[:-1],s2,s3[:-1]) or self.isInterleave(s1,s2[:-1],s3[:-1])
        elif s1 and s3[-1]==s1[-1]:
            return self.isInterleave(s1[:-1], s2, s3[:-1])
        elif s2 and s3[-1]==s2[-1]:
            return self.isInterleave(s1,s2[:-1],s3[:-1])
        else:
            return False

    def isInterleave2(self, s1: str, s2: str, s3: str) -> bool:
        len1 = len(s1)
        len2 = len(s2)

        if len2+len1!=len(s3):
            return False

        dp = [[False]*(len1+1) for _ in range(len2+1)]
        dp[0][0] = True
        for i in range(len2+1):
            for j in range(len1+1):
                p = i+j-1
                if i>0:
                    dp[i][j] = (dp[i-1][j] & (s2[i-1]==s3[p]))
                if j>0:
                    dp[i][j] = dp[i][j] | (dp[i][j-1] & (s1[j - 1] == s3[p]))
        return dp[-1][-1]


if __name__ == '__main__':
    s1 = "aabcc"
    s2 = "dbbca"
    s3 = "aadbbcbcac"
    sol = Solution()
    print(sol.isInterleave2(s1,s2,s3))

