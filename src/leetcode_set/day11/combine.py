# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-03-21
    FileName   : combine.py
    Author     : Honghe
    Descreption: 77. 组合
"""
import copy

class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        res = []
        self.combine_list(1,n+1,k,[],res)
        return res


    def combine_list(self,start, end, k,tmp_list,res):
        if end-start<k-len(tmp_list):
            return
        for i in range(start,end):
            tmp_list.append(i)
            if len(tmp_list)==k and tmp_list not in res:
                res.append(copy.deepcopy(tmp_list))
            else:
                self.combine_list(i + 1, end, k, tmp_list, res)
            tmp_list.pop()



if __name__ == '__main__':
    sol = Solution()
    n = 1
    k = 1
    print(sol.combine(n,k))