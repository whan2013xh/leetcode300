# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-07-20
    FileName   : findOrder.py
    Author     : Honghe
    Descreption: 
"""
from typing import List
from collections import deque,defaultdict

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        """
        bfs:构建有向图+每个节点入度值
        :param numCourses:
        :param prerequisites:
        :return:
        """
        length = len(prerequisites)
        if length==0:
            return list(range(numCourses))

        need_course=[0]*numCourses
        edage = defaultdict(list)
        for i,j in prerequisites:
            need_course[i]+=1
            edage[j].append(i)

        first_course = [index for index,i in enumerate(need_course) if i==0]
        level_course = deque(first_course)
        res = []
        while level_course:
            course = level_course.popleft()
            res.append(course)
            for i in edage[course]:
                need_course[i]-=1
                if need_course[i]==0:
                    level_course.append(i)
        return res if len(res)==numCourses else []



if __name__ == '__main__':
    sol = Solution()
    numCourses = 4
    prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]]
    print(sol.findOrder(numCourses,prerequisites))




