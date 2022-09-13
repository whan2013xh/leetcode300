# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-08-02
    FileName   : intersection-1603.py
    Author     : Honghe
    Descreption: 
"""
from typing import List

class Solution:
    def intersection(self, start1: List[int], end1: List[int], start2: List[int], end2: List[int]) -> List[float]:
        """
        几何方程：已知两个点(a1,b1)，(a2,b2)直线方程式 y=b1 if a1==a2 else y-b2 = (b2-b1)/(a2-a1)*x
        两条直线平行，斜率K相等
        两条直线相交，求交点解方程即可
        :param start1:
        :param end1:
        :param start2:
        :param end2:
        :return:
        """
        a1,b1 = start1
        a2,b2 = end1
        c1,d1 = start2
        c2,d2 = end2
        # 1、两个直线平行
        if (a1-a2)*(d1-d2)-(b1-b2)*(c1-c2)==0:
            # 如果是垂直于X轴的
            if a1==a2:
                if a1!=c1 or max(b1,b2)<min(d1,d2) or min(b1,b2)>max(d1,d2):
                    return []
                else:
                    return [a1,max(min(b1,b2),min(d1,d2))]
            else:
                # 判断平行直线是不是一条
                if (a1!=c1 and abs((b1-b2)/(a1-a2))!=abs((b1-d1)/(a1-c1))) or max(b1,b2)<min(d1,d2) or min(b1,b2)>max(d1,d2):
                    return []
                else:
                    return [max(min(a1, a2), min(c1, c2)), max(min(b1, b2), min(d1, d2))]
        x = ((a2 - a1) * (c2 - c1) * (d2 - b2) + (b2 - b1) * (c2 - c1) * a2 - (d2 - d1) * (a2 - a1) * c2) / (
                    (b2 - b1) * (c2 - c1) - (d2 - d1) * (a2 - a1))
        y = (b2 - b1) / (a2 - a1) * (x - a2) + b2 if a2!=a1 else (d2 - d1) / (c2 - c1) * (x - c2) + d2
        # 2、直线相交，判断相交点是否在直线上
        if min(a1,a2)<=x<=max(a1,a2) and min(b1,b2)<=y<=max(b1,b2) and min(c1,c2)<=x<=max(c1,c2) and min(d1,d2)<=y<=max(d1,d2):
            return [x,y]
        return []

if __name__ == '__main__':
    sol = Solution()
    start1 = [0, 0]
    end1 = [1, -1]
    start2 = [0, 0]
    end2 = [-1, 1]
    print(sol.intersection(start1,end1,start2,end2))


