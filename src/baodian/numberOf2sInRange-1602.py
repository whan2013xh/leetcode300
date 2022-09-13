# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-08-04
    FileName   : numberOf2sInRange-1602.py
    Author     : Honghe
    Descreption: 
"""

class Solution:
    def numberOf2sInRange(self, n: int) -> int:
        """
        数学规律:其实会发现10、100、1000、10000包含的2的个数呈现的趋势
        :param n:
        :return:
        """
        nums = {
            0:0,
            1:1,
            2:20,
            3:300,
            4:4000,
            5:50000,
            6:600000,
            7:7000000,
            8:80000000,
            9:900000000
        }
        res = 0
        n = str(n)
        length = len(n)
        for i in range(len(n)):
            cur = int(n[i])
            if cur==0:
                continue
            if cur==1:
                res += nums[length-i-1]
            elif cur>2:
                res += nums[length-i-1]*cur+10**(length-i-1)
            else:
                res += nums[length-i-1]*2+int(n[i+1:])+1 if i+1<length else 1
        return res

if __name__ == '__main__':
    sol = Solution()
    n=1000000000
    print(sol.numberOf2sInRange(n))


