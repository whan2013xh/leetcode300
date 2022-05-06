# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-04-22
    FileName   : longestPalindrome.py
    Author     : Honghe
    Descreption: 5. 最长回文子串
"""

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        s_len = len(s)
        dp = [[0]*s_len for _ in range(s_len)]
        start = 0
        end=0
        max_length = 1
        for i in range(s_len):
            dp[i][i] = 1

        for i in range(s_len-1,-1,-1):
            for j in range(i+1,s_len):
                if s[i]==s[j]:
                    if j-i<3 or dp[i+1][j-1]==(j-i-1):
                        dp[i][j] = dp[i+1][j-1]+2
                        if max_length<dp[i][j]:
                            max_length = dp[i][j]
                            start = i
                            end = j
                    else:
                        dp[i][j] = max(dp[i][j-1],dp[i+1][j])
                else:
                    dp[i][j] = max(dp[i][j-1],dp[i+1][j])
        return s[start:end+1]

    def longestPalindrome2(self, s):
        s_len = len(s)
        dp = [[False] * s_len for _ in range(s_len)]
        start = 0
        max_length = 1
        # 枚举子串长度
        for L in range(2,s_len+1):
            # 遍历子串起始位置
            for i in range(s_len):
                # 子串结尾
                j = L+i-1
                if j>s_len-1:
                    break
                if s[i]==s[j]:
                    if j-i<3:
                        dp[i][j] = True
                    else:
                        dp[i][j]=dp[i+1][j-1]
                else:
                    dp[i][j] = False
                if dp[i][j] and j-i>max_length-1:
                    start = i
                    max_length = j-i+1
        return s[start:start+max_length]

    def longestPalindrome3(self, s):
        max_length = 1
        start = 0
        for i in range(len(s)):
            start1,end1 = self.middle(s,i,i)
            start2,end2 = self.middle(s,i,i+1)
            if end1-start1+1>max_length:
                max_length = end1-start1
                start = start1
            if end2 - start2 + 1 > max_length:
                max_length = end2 - start2
                start = start2
        return s[start:start+max_length+1]



    def middle(self,s,left,right):
        while left>=0 and right<len(s) and s[left]==s[right]:
            left -=1
            right +=1
        return left+1,right-1

    def longestPalindrome4(self, s):
        """
        只需要从头到尾扫描，一次添加一个字符，跟踪maxPalindromeLen，
        并为每个添加的字符，检查以这个新字符结尾的子字符串，长度为P + 1或P + 2，是回文，并相应更新。
        :type s: str
        :rtype: str
        """
        if len(s) == 0:
            return ""
        maxPalindrome = 1
        start = 0
        for i in range(len(s)):
            # 一种场景是添加最新的字符，让回文字符串增加2，这个时候会存在i - maxPalindrome >= 1
            if i - maxPalindrome >= 1 and s[i - maxPalindrome - 1:i + 1] == s[i - maxPalindrome - 1:i + 1][::-1]:
                start = i - maxPalindrome - 1
                maxPalindrome += 2
                continue
            # 一种场景是添加最新的字符，让回文字符串增加1，这个时候会存在i - maxPalindrome >= 0
            if i - maxPalindrome >= 0 and s[i - maxPalindrome:i + 1] == s[i - maxPalindrome:i + 1][::-1]:
                start = i - maxPalindrome
                maxPalindrome += 1
        return s[start:start + maxPalindrome]


if __name__ == '__main__':
    sol = Solution()
    s = "bbbb"
    print(sol.longestPalindrome3(s))
