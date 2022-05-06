# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-04-24
    FileName   : wordBreak.py
    Author     : Honghe
    Descreption: 139. 单词拆分
"""

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        path = {}
        return self.dfs(s,wordDict,path)

    def dfs(self,s,wordDict,path):
        if not s:
            return True
        if path.get(s) is not None:
            return path.get(s)
        for i in wordDict:
            if s[:len(i)]==i:
                res = self.wordBreak(s[len(i):],wordDict)
                path[s[len(i):]] = res
                if res:
                    return True
        return False

    def wordBreak2(self, s, wordDict):
        dp = [False]*(len(s)+1)
        dp[0]= True
        for index,word in enumerate(s):
            for j in range(index+1,len(s)+1):
                if dp[index] and s[index:j] in wordDict:
                    dp[j]=True
        return dp[-1]

if __name__ == '__main__':
    s = "catsandog"
    wordDict = ["cats", "og", "sand", "and", "cat"]
    sol = Solution()
    print(sol.wordBreak2(s,wordDict))
