# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-04-11
    FileName   : intervalIntersection.py
    Author     : Honghe
    Descreption: 986. 区间列表的交集
"""

class Solution(object):
    def intervalIntersection(self, firstList, secondList):
        """
        :type firstList: List[List[int]]
        :type secondList: List[List[int]]
        :rtype: List[List[int]]
        """
        if not (firstList and secondList):
            return []
        res = []
        first_pos = 0
        i=0
        j=0
        while i<len(firstList) and j<len(secondList):
            first_pos = max(first_pos, firstList[i][0],secondList[j][0])
            if firstList[i][1]>secondList[j][1]:
                second_pos = secondList[j][1]
                j+=1
            else:
                second_pos = firstList[i][1]
                i+=1
            if first_pos<=second_pos:
                res.append([first_pos,second_pos])
        return res

if __name__ == '__main__':
    sol = Solution()
    firstList = [[0, 2], [5, 10], [13, 23], [24, 25]]
    secondList = [[1, 5], [8, 12], [15, 24], [25, 26]]
    print(sol.intervalIntersection(firstList,secondList))

