# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-05-05
    FileName   : divide.py
    Author     : Honghe
    Descreption: 剑指 Offer II 001. 整数除法
"""

class Solution(object):
    def divide(self, a, b):
        """
        二项式展开，需要注意返回结果在-2**31到2**31-1之间
        :type a: int
        :type b: int
        :rtype: int
        """
        res = 0
        flag = 1
        INT_MIN, INT_MAX = -2 ** 31, 2 ** 31 - 1

        # 考虑被除数为最小值的情况
        if a == INT_MIN:
            if b == 1:
                return INT_MIN
            if b == -1:
                return INT_MAX

        # 考虑除数为最小值的情况
        if b == INT_MIN:
            return 1 if a == INT_MIN else 0
        if a<0:
            a = -a
            flag = -flag
        if b <0:
            b = -b
            flag = -flag
        if a<b:
            return 0

        # 考虑被除数为 0 的情况
        if a == 0:
            return 0
        tmp = b
        pos = 0
        tmp_list = []
        while a>=tmp:
            if a==tmp:
                return 2 ** pos if flag>0 else -(2 ** pos)
            tmp_list.append(tmp)
            tmp = tmp<<1
            pos += 1
        count = len(tmp_list)
        for index,num in enumerate(tmp_list[::-1]):
            if a>=num:
                a -= num
                res += 2**(count-index-1)
                if a==0:
                    return res if flag>0 else -res
        return res if flag>0 else -res

if __name__ == '__main__':
    sol = Solution()
    a = -2147483648
    b = -1
    print(sol.divide(a,b))


