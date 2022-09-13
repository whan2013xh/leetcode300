# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-06-17
    FileName   : evalRPN.py
    Author     : Honghe
    Descreption: 剑指 Offer II 036. 后缀表达式
"""


class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        for index,token in enumerate(tokens):
            if token.isdigit() or (token[0]=="-" and token[1:].isdigit()):
                stack.append(int(token))
            else:
                num2 = stack.pop()
                num1 = stack.pop()
                if token=="+":
                    tmp_res = num1+num2
                elif token=="-":
                    tmp_res = num1 - num2
                elif token=="/":
                    tmp_res = int(num1 / num2)
                elif token=="*":
                    tmp_res = num1 * num2
                stack.append(tmp_res)
        return stack[0]








if __name__ == '__main__':
    sol = Solution()
    tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
    print(sol.evalRPN2(tokens))

