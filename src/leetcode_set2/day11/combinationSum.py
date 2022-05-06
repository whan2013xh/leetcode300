# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-04-19
    FileName   : combinationSum.py
    Author     : Honghe
    Descreption: 39. 组合总和
"""
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        res = []
        self.back_trace(candidates,target,res,[],0)
        return res


    def back_trace(self, candidates, target, res, tmp,begin):
        if target==0 and tmp not in res:
            res.append(tmp[:])
            return

        for index,num in enumerate(candidates[begin:]):
            if num>target:
                return
            tmp.append(num)
            self.back_trace(candidates,target-num,res,tmp,begin+index)
            tmp.pop()


if __name__ == '__main__':
    sol = Solution()
    candidates = [2, 3, 6,7]
    target = 7
    print(sol.combinationSum(candidates,target))
