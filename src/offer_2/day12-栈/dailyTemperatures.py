# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-06-17
    FileName   : dailyTemperatures.py
    Author     : Honghe
    Descreption: 剑指 Offer II 038. 每日温度
"""


class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        暴力法
        :type temperatures: List[int]
        :rtype: List[int]
        """
        res = []

        for index,i in enumerate(temperatures[:-1]):
            dif = 0
            for index2,j in enumerate(temperatures[index+1:]):
                if j>i:
                    dif = index2+1
                    break
            res.append(dif)
        res.append(0)
        return res

    def dailyTemperatures2(self, tokens):
        """
        单调栈
        :type tokens: List[str]
        :rtype: int
        """
        length = len(tokens)
        res = [0]*length
        stack = []
        for i in range(length):
            while stack and tokens[stack[-1]]<tokens[i]:
                prev_index = stack.pop()
                res[prev_index] = i-prev_index
            stack.append(i)
        return res

if __name__ == '__main__':
    sol = Solution()
    temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
    print(sol.dailyTemperatures(temperatures))












