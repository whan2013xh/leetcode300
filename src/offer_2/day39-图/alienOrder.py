# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-07-21
    FileName   : alienOrder.py
    Author     : Honghe
    Descreption: 
"""
from typing import List
from collections import deque

class Solution:
    def alienOrder(self, words: List[str]) -> str:
        """
        拓扑排序+bfs:
        1、统计
        :param words:
        :return:
        """
        if len(words)==1:
            return words[0]
        res = []
        order = [[False]*26 for _ in range(26)]
        chars = [False]*26
        count = 0
        # 1、统计出现的字符
        # 2、将两两字符先后顺序标记出来，当做构建图的边，方便后面拓扑排序
        for i in range(len(words)-1):
            for j in words[i]:
                if count>=26:
                    break
                index = ord(j)-ord('a')
                if not chars[index]:
                    chars[index]=True
                    count+=1

            cur_word = words[i]
            next_word = words[i+1]
            for j in range(len(cur_word)):
                if j>=len(next_word):
                   return ""
                cur_char = ord(cur_word[j])-ord('a')
                next_char = ord(next_word[j])-ord('a')
                if cur_char==next_char:
                    continue
                if order[next_char][cur_char]:
                    return ""
                order[cur_char][next_char] = True
                break

        # 最后一个单词统计
        for j in words[-1]:
            if count >= 26:
                break
            index = ord(j) - ord('a')
            if not chars[index]:
                chars[index] = True
                count += 1
        #3、计算每个几点入度
        in_degree = [0]*26
        for i in range(26):
            for j in range(26):
                if i!=j and chars[i] and order[i][j]:
                    in_degree[j]+=1

        # 4、将出现过的入度为0的字符添加进队列
        first_chars = [i for i in range(26) if chars[i] and in_degree[i]==0]
        queue = deque(first_chars)
        while queue:
            cur = queue.popleft()
            res.append(chr(cur+ord('a')))
            for i in range(26):
                if cur!=i and chars[i] and order[cur][i]:
                    in_degree[i]-=1
                    if in_degree[i]==0:
                        queue.append(i)
        return "".join(res) if len(res)==count else ""

if __name__ == '__main__':
    sol = Solution()
    words = ["z","x","z"]
    print(sol.alienOrder(words))




