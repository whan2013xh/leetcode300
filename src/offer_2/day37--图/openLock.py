# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-07-19
    FileName   : openLock.py
    Author     : Honghe
    Descreption: 
"""
from typing import List
from collections import deque

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends = set(deadends)

        start = "0000"
        if start in deadends:
            return -1
        if target==start:
            return 0
        queue = deque([start])
        visited = set([start])
        step = 0

        while queue:
            length = len(queue)
            for i in range(length):
                node = queue.popleft()
                tmp = list(node)
                for j in range(len(node)):
                    for k in [-1,1]:
                        next_num = int(tmp[j])+k
                        if next_num==-1:
                            tmp[j] = str(9)
                        elif next_num==10:
                            tmp[j] = str(0)
                        else:
                            tmp[j] = str(next_num)
                        tmp_node = "".join(tmp)
                        tmp[j] = node[j]
                        if tmp_node in deadends:
                            continue
                        if tmp_node==target:
                            return step+1
                        if tmp_node not in visited:
                            queue.append(tmp_node)
                            visited.add(tmp_node)

            step+=1
        return -1

    def openLock2(self, deadends: List[str], target: str) -> int:
        """
        双向bfs
        :param deadends:
        :param target:
        :return:
        """
        deadends = set(deadends)
        start = "0000"
        if start in deadends:
            return -1
        if target==start:
            return 0

        start_visited = set([start])
        end_visited = set([target])
        visited = set([start])
        step = 0

        while start_visited and end_visited:
            if len(start_visited)>len(end_visited):
                start_visited,end_visited = end_visited,start_visited

            level_node = set()
            for node in start_visited:
                tmp = list(node)
                for j in range(len(node)):
                    for k in [-1, 1]:
                        next_num = int(tmp[j]) + k
                        if next_num == -1:
                            tmp[j] = str(9)
                        elif next_num == 10:
                            tmp[j] = str(0)
                        else:
                            tmp[j] = str(next_num)
                        tmp_node = "".join(tmp)
                        tmp[j] = node[j]
                        if tmp_node in deadends:
                            continue
                        if tmp_node in end_visited:
                            return step + 1
                        if tmp_node not in visited:
                            level_node.add(tmp_node)
                            visited.add(tmp_node)
            start_visited = level_node
            step+=1
        return -1




if __name__ == '__main__':
    deadends = ["0201","0101","0102","1212","2002"]
    target = "0202"
    sol = Solution()
    print(sol.openLock2(deadends,target))

