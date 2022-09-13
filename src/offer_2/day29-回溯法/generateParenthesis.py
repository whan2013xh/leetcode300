# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-07-06
    FileName   : generateParenthesis.py
    Author     : Honghe
    Descreption: 剑指 Offer II 085. 生成匹配的括号
"""
from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        path = []
        nums = ["("]*n+[")"]*n
        visited = [False]*(2*n)
        # self.back_track(nums,res,path,0,0,visited)
        self.back_track2(n, res, path, 0, 0)
        return res

    def back_track(self,nums,res,path,left_count,right_count,visited):
        if len(path)==len(nums) and left_count==right_count:
            res.append("".join(path[:]))
            return

        for i in range(len(nums)):
            if visited[i] or (i>0 and nums[i]==nums[i-1] and not visited[i-1]):
                continue

            if left_count<=right_count and nums[i]==")":
                break

            path.append(nums[i])
            visited[i]=True
            if nums[i]=="(":
                left_count+=1
            else:
                right_count+=1
            self.back_track(nums,res,path,left_count,right_count,visited)
            path.pop()
            visited[i]=False
            if nums[i]=="(":
                left_count-=1
            else:
                right_count-=1

    def back_track2(self, n,res, path, left_count, right_count):
        if len(path)==2*n:
            res.append("".join(path))
            return

        if left_count<n:
            path.append("(")
            left_count+=1
            self.back_track2(n,res,path,left_count,right_count)
            left_count-=1
            path.pop()
        if right_count<left_count:
            path.append(")")
            self.back_track2(n,res,path,left_count,right_count+1)
            path.pop()





if __name__ == '__main__':
    sol = Solution()
    n = 1
    print(sol.generateParenthesis(n))