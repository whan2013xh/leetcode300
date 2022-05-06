# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-04-26
    FileName   : minDistance.py
    Author     : Honghe
    Descreption: 72. 编辑距离
"""

class Solution(object):
    def minDistance(self, word1, word2):
        """
        自顶向下
        :type word1: str
        :type word2: str
        :rtype: int
        """
        if not word1:
            return len(word2)
        if not word2:
            return len(word1)
        meto = [[-1]*(len(word2)) for _ in range(len(word1))]
        self.dp(word1,len(word1)-1,word2,len(word2)-1,meto)
        return meto[-1][-1]


    def dp(self,word1,pos1,word2,pos2,meto):
        if pos1==-1:
            return pos2+1
        if pos2==-1:
            return pos1+1
        if meto[pos1][pos2]!=-1:
            return meto[pos1][pos2]
        if word1[pos1]==word2[pos2]:
            meto[pos1][pos2] = self.dp(word1,pos1-1,word2,pos2-1,meto)
        else:
            meto[pos1][pos2] = min(self.dp(word1,pos1-1,word2,pos2,meto),self.dp(word1,pos1,word2,pos2-1,meto),self.dp(word1,pos1-1,word2,pos2-1,meto))+1
        return meto[pos1][pos2]

    def minDistance2(self, word1, word2):
        """
        自底向上
        :type word1: str
        :type word2: str
        :rtype: int
        """
        dp = [[0]*(len(word2)+1) for _ in range(len(word1)+1)]
        for i in range(len(word1)+1):
            dp[i][0] = i
        for j in range(len(word2)+1):
            dp[0][j] = j
        for i in range(1,len(word1)+1):
            for j in range(1,len(word2)+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])+1
        return dp[-1][-1]



if __name__ == '__main__':
    sol =  Solution()
    word1 = "intention"
    word2 = "execution"
    print(sol.minDistance2(word1,word2))