# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-07-27
    FileName   : longestConsecutive.py
    Author     : Honghe
    Descreption: 128. 最长连续序列
"""
from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        并查集
        :param nums:
        :return:
        """
        if not nums:
            return 0
        parents = list(range(len(nums)))
        size = [1]*len(nums)
        count = {}
        for index,num in enumerate(nums):
            if num in count:
                continue
            if num+1 in count:
                parents[index] = self.find(count[num+1],parents)
                size[parents[index]] += 1
            if num-1 in count:
                size[parents[index]] += size[self.find(count[num - 1], parents)]
                parents[self.find(count[num-1],parents)] = parents[index]
            count[num]=index
        return max(size)

    def find(self,node,parents):
        father = parents[node]
        if father!=node:
            parents[node]=self.find(father,parents)
        return parents[node]

    def longestConsecutive2(self, nums: List[int]) -> int:
        """
        哈希表
        :param nums:
        :return:
        """
        count = set(nums)
        res= 0
        for num in count:
            if num-1 not in count:
                tmp=1
                cur = num
                while cur+1 in count:
                    tmp+=1
                    cur = cur+1
                res = max(res,tmp)
        return res


if __name__ == '__main__':
    sol = Solution()
    nums = [1,2,0,1]
    print(sol.longestConsecutive2(nums))
