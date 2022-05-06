# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-04-19
    FileName   : combinationSum2.py
    Author     : Honghe
    Descreption: 40. 组合总和 II
"""

class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        res = []
        self.back_trace(candidates, target, res, [], 0)
        return res

    def back_trace(self, candidates, target, res, tmp, begin):
        if target == 0 and tmp not in res:
            res.append(tmp[:])
            return
        if sum(candidates[begin:])<target:
            return

        for index, num in enumerate(candidates[begin:]):
            if num > target:
                return
            if index>0 and num ==candidates[index+begin-1]:
                continue
            tmp.append(num)
            self.back_trace(candidates, target - num, res, tmp, begin + index+1)
            tmp.pop()

    def combinationSum3(self, candidates, target) :
        def dfs(begin, path, residue):
            if residue == 0:
                res.append(path[:])
                return

            for index in range(begin, size):
                if candidates[index] > residue:
                    break

                if index > begin and candidates[index - 1] == candidates[index]:
                    continue

                path.append(candidates[index])
                dfs(index + 1, path, residue - candidates[index])
                path.pop()

        size = len(candidates)
        if size == 0:
            return []

        candidates.sort()
        res = []
        dfs(0, [], target)
        return res


if __name__ == '__main__':
    sol = Solution()
    candidates=[10,1,2,7,6,1,5]
    target = 8
    print(sol.combinationSum2(candidates,target))