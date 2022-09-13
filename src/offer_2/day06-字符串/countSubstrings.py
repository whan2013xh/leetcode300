# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-06-07
    FileName   : countSubstrings.py
    Author     : Honghe
    Descreption: 剑指 Offer II 020. 回文子字符串的个数
"""

class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = len(s)
        res = []
        for index,letter in enumerate(s):
            flag = True
            odd_flag = True
            res.append(letter)
            for window_size in range(2,2*index+2+1):
                if window_size//2<len(s)-index:
                    if window_size%2==0:
                        if not flag:
                            continue
                        if s[index]!=s[index+1]:
                            flag=False
                        else:
                            flag = self.is_palindrome(s[index-window_size//2+1:index+window_size//2+1])
                            if flag:
                               count+=1
                               res.append(s[index-window_size//2+1:index+window_size//2+1])
                    else:
                        if not odd_flag:
                            continue
                        odd_flag = self.is_palindrome(s[index-window_size//2:index+window_size//2+1])
                        if odd_flag:
                            count += 1
                            res.append(s[index - window_size // 2:index + window_size // 2+1])
                    if not flag and not odd_flag:
                        break
                else:
                    break
        return count


    def is_palindrome(self, s):
            return s == s[::-1]

    def countSubstrings2(self, s):
        """
        中心拓展法
        :type s: str
        :rtype: int
        """
        n = len(s)
        res =0
        for i in range(0,2*n-1):
            left = i//2
            right = i//2+i%2
            while (left>=0 and right<n and s[left]==s[right]):
                left-=1
                right+=1
                res+=1
        return res


if __name__ == '__main__':
    sol = Solution()
    s = "abc"
    print(sol.countSubstrings(s))
