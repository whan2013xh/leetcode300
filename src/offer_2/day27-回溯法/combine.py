# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-07-05
    FileName   : combine.py
    Author     : Honghe
    Descreption: 剑指 Offer II 080. 含有 k 个元素的组合
"""
from typing import List

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        path = []
        visited = [False]*n
        # self.trace(n,k,res,path)
        self.back_track(n,k,res,path,1,visited)
        return res

    def trace(self,n,k,num_list,path):
        if n<k:
            return
        if k==0:
           num_list.append(path[:])
           return

        self.trace(n-1,k,num_list,path)
        path.append(n)
        self.trace(n-1,k-1,num_list,path)
        path.pop()

    def back_track(self,n,k,num_list,path,index,visited):
        if n-index+1<k:
            return
        if k==0:
           num_list.append(path[:])
           return

        for i in range(index,n+1):
            if visited[i-1]:
                continue
            path.append(i)
            visited[i-1]=True
            self.back_track(n,k-1,num_list,path,i+1,visited)
            visited[i - 1] = False
            path.pop()

if __name__ == '__main__':
    sol = Solution()
    n=4
    k=2
    print(sol.combine(n,k))