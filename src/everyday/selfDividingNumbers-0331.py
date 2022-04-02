# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-03-31
    FileName   : selfDividingNumbers-0331.py
    Author     : Honghe
    Descreption: 728. 自除数
"""
class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        res = []
        for num in range(left,right+1):
            if num<10:
                res.append(num)
                continue
            tmp = str(num)
            flag = True
            for i in tmp:
                if int(i)==0:
                    flag = False
                    break
                elif num%int(i)!=0:
                    flag = False
                    break
            if flag:
                res.append(num)
        return res

if __name__ == '__main__':
    sol = Solution()
    left = 1
    right = 22
    print(sol.selfDividingNumbers(left,right))