# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-03-15
    FileName   : floodFill.py
    Author     : Honghe
    Descreption: 733. 图像渲染
"""

class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        pos = []
        pos.append([sr,sc])
        row = len(image)
        col = len(image[0])
        tmp_color = image[sr][sc]
        visited = []
        while pos:
            cur = pos.pop(0)
            tmp_sr,tmp_sc = cur
            image[tmp_sr][tmp_sc] = newColor
            round_pos = [[tmp_sr-1,tmp_sc],[tmp_sr+1,tmp_sc],[tmp_sr,tmp_sc-1],[tmp_sr,tmp_sc+1]]
            for i,j in round_pos:
                if [i,j] in visited:
                    continue
                else:
                    visited.append([i,j])
                if 0<=i<row and 0<=j<col and image[i][j]==tmp_color:
                    image[i][j]=newColor
                    pos.append([i,j])
        return image

if __name__ == '__main__':
    sol = Solution()
    image = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
    sr = 1
    sc = 1
    newColor = 2
    print(sol.floodFill(image,sr,sc,newColor))