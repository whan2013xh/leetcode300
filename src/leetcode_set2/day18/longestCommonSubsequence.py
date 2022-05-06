# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-04-25
    FileName   : longestCommonSubsequence.py
    Author     : Honghe
    Descreption: 1143. 最长公共子序列
"""

class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        自顶向下
        :type text1: str
        :type text2: str
        :rtype: int
        """
        meto = [[-1]*len(text2) for _ in range(len(text1))]
        return self.dp(text1,0,text2,0,meto)


    def dp(self,text1,pos1,text2,pos2,meto):
        if pos1==len(text1):
            return 0
        if pos2==len(text2):
            return 0
        if meto[pos1][pos2]!=-1:
            return meto[pos1][pos2]
        if text1[pos1]==text2[pos2]:
            meto[pos1][pos2] = self.dp(text1,pos1+1,text2,pos2+1,meto)+1
        else:
            meto[pos1][pos2] = max(self.dp(text1,pos1+1,text2,pos2,meto),self.dp(text1,pos1,text2,pos2+1,meto))
        return meto[pos1][pos2]

    def longestCommonSubsequence2(self, text1, text2):
        """
        自底向上
        :type text1: str
        :type text2: str
        :rtype: int
        """
        dp = [[0] * (len(text2)+1) for _ in range(len(text1)+1)]
        for i in range(1,len(text1)+1):
            for j in range(1,len(text2)+1):
                if text1[i-1]==text2[j-1]:
                    dp[i][j]=dp[i-1][j-1]+1
                else:
                    dp[i][j] = max(dp[i-1][j],dp[i][j-1])
        return dp[-1][-1]





if __name__ == '__main__':
    sol = Solution()
    text1 = "abcde"
    text2 = "acd"
    print(sol.longestCommonSubsequence2(text1,text2))
