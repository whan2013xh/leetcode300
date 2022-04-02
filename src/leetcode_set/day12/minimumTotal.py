# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-04-02
    FileName   : minimumTotal.py
    Author     : Honghe
    Descreption: 120. 三角形最小路径和
"""
class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        for index,level in enumerate(triangle):
            for index2 in range(index+1):
                if index==0:
                    continue
                if index2==0:
                    triangle[index][index2] = triangle[index - 1][0] + triangle[index][index2]
                elif index2==len(level)-1:
                    triangle[index][index2]=triangle[index-1][-1]+triangle[index][index2]
                else:
                    triangle[index][index2] = min(triangle[index-1][index2],triangle[index-1][index2-1])+triangle[index][index2]
        return min(triangle[-1])

if __name__ == '__main__':
    sol = Solution()
    triangle = [[-1]]
    print(sol.minimumTotal(triangle))

