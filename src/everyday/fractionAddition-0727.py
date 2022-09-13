# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-07-28
    FileName   : fractionAddition-0727.py
    Author     : Honghe
    Descreption: 592. 分数加减运算
"""


class Solution:
    def fractionAddition(self, expression: str) -> str:
        """
        双栈求解表达式
        :param expression:
        :return:
        """
        num1 = []
        num2 = []
        start = 0
        for index,char in enumerate(expression):
            if char=="/":
                num1.append(int(expression[start:index]))
                start = index+1
            elif char=="+" or (char=="-" and start!=0):
                num2.append(int(expression[start:index]))
                start = index+1 if char=="+" else index
        num2.append(int(expression[start:]))
        total = 1
        for i in num2:
            total*=i
        for index in range(len(num2)):
            num1[index] *= total//num2[index]
        res = sum(num1)
        tmp = min(abs(res),abs(total))
        if res==0:
            return "0/1"
        for i in range(tmp,0,-1):
            if res%i==0 and total%i==0:
                return str(res//i)+"/"+str(total//i)
        return str(res)+"/"+str(total)

if __name__ == '__main__':
    sol = Solution()
    expression = "-1/4-4/5-1/4"
    print(sol.fractionAddition(expression))



