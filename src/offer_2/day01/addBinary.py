# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-05-06
    FileName   : addBinary.py
    Author     : Honghe
    Descreption: 剑指 Offer II 002. 二进制加法
"""

class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        res = str(int(a)+int(b))
        tmp = []
        add_flag = False
        for i in res[::-1]:
            if int(i)==2:
                if add_flag:
                    tmp.append("1")
                else:
                    add_flag = True
                    tmp.append("0")
            elif int(i)==1:
                if add_flag:
                    tmp.append("0")
                else:
                    tmp.append("1")
            else:
                if add_flag:
                    tmp.append("1")
                    add_flag = False
                else:
                    tmp.append("0")
        if add_flag:
            tmp.append("1")
        return "".join(tmp[::-1])

if __name__ == '__main__':
    sol = Solution()
    a = "1010"
    b = "1011"
    print(sol.addBinary(a,b))
