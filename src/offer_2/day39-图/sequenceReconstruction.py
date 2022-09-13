# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-07-21
    FileName   : sequenceReconstruction.py
    Author     : Honghe
    Descreption: 重建序列444 题相同：https://leetcode.cn/problems/sequence-reconstruction/
"""
from typing import List
from collections import deque,defaultdict

class Solution:
    def sequenceReconstruction(self, org: List[int], seqs: List[List[int]]) -> bool:
        """
        拓扑排序+bfs
        :param org:
        :param seqs:
        :return:
        """
        # 1、构建图，这么解空间复杂度会比较高，因为len(org)可以很大
        visited = [False]*len(org)
        edage = defaultdict(set)
        for i in range(len(seqs)):
            seq = seqs[i]
            for j in range(len(seq)):
                num = seq[j]
                if num<1 or num>len(org):
                    return False
                visited[num-1]=True
                if j!=len(seq)-1:
                    next_num = seq[j+1]
                    edage[num].add(next_num)

        if sum(visited)<len(org):
            return False
        # 2、计算入度和出度
        in_degree = [0]*len(org)
        for key,value in edage.items():
            for j in value:
                in_degree[j-1]+=1

        start = [index+1 for index,val in enumerate(in_degree) if val==0]
        queue = deque(start)
        count = 0
        while queue:
            if len(queue)!=1:
                return False
            cur = queue.popleft()
            if (cur)!=org[count]:
                return False
            for i in edage[cur]:
                in_degree[i-1]-=1
                if in_degree[i-1]==0:
                    queue.append(i)
            count+=1
        return count==len(org)

if __name__ == '__main__':
    sol = Solution()
    org = [1,2,3]
    seqs = [[1,2],[1,3],[2,3]]
    print(sol.sequenceReconstruction(org,seqs))





