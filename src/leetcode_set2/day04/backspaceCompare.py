# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-04-11
    FileName   : backspaceCompare.py
    Author     : Honghe
    Descreption: 844. 比较含退格的字符串
"""

class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s1 = self.get_str(s)
        t1 = self.get_str(t)
        return s1==t1


    def get_str(self,s):
        res = []
        for i in s:
            if i!="#":
                res.append(i)
            else:
                if len(res)>=1:
                    res.pop(-1)
        return "".join(res)


    def backspaceCompare2(self, s, t):
        """
        双指针解法
        :param s:
        :param t:
        :return:
        """
        skip1 = 0
        skip2 = 0
        i= len(s)-1
        j = len(t)-1
        while i>=0 and j>=0:
            while i>=0:
                if s[i]=="#":
                    skip1 += 1
                    i -=1
                elif skip1>0:
                    skip1-=1
                    i-=1
                else:
                    break
            while j>=0:
                if s[j]=="#":
                    skip2 += 1
                    j -=1
                elif skip2>0:
                    skip2-=1
                    j-=1
                else:
                    break

            if i>=0 and j>=0:
                if s[i]!=t[j]:
                    return False
            else:
                return False

            i-=1
            j-=1
        return True






if __name__ == '__main__':
    sol = Solution()
    s = "ab#c"
    t = "ad#c"
    print(sol.backspaceCompare(s,t))
