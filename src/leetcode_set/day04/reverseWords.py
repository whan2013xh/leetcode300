# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-03-14
    FileName   : reverseWords.py
    Author     : Honghe
    Descreption: 557. 反转字符串中的单词 III
"""

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        words = s.split()
        for index, word in enumerate(words):
            tmp = self.reverse(list(word))
            words[index] = tmp
        return " ".join(words)

    def reverse(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        left = 0
        right = len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        return "".join(s)


if __name__ == '__main__':
    s = "Let's take LeetCode contest"
    sol = Solution()
    res = sol.reverseWords(s)
    print(res)
