# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-04-20
    FileName   : generateParenthesis.py
    Author     : Honghe
    Descreption: 22. 括号生成
"""


class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        self.back_trace(n,n,res,[])
        return res

    def back_trace(self,left,right,res,tmp):
        if left==0 and right==0:
            res.append("".join(tmp))
            return
        if left>0:
            tmp.append("(")
            self.back_trace(left-1,right,res,tmp)
            tmp.pop()
        if right>left:
            tmp.append(")")
            self.back_trace(left, right-1, res, tmp)
            tmp.pop()


if __name__ == '__main__':
    sol = Solution()
    n=3
    print(sol.generateParenthesis(n))
