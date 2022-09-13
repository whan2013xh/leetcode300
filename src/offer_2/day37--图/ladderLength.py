# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-07-14
    FileName   : ladderLength.py
    Author     : Honghe
    Descreption: 
"""
from typing import List
from collections import defaultdict,deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        """
        广度优先搜索
        :param beginWord:
        :param endWord:
        :param wordList:
        :return:
        """
        words = defaultdict()
        wordList = set(wordList)

        for i in wordList:
            words[i] = []
        if endWord not in words:
            return 0
        letters = "abcdefghijklmnopqrstuvwxyz"

        queue = deque()
        visited = set()
        queue.append(beginWord)
        visited.add(beginWord)
        step=1
        while queue:
            level = len(queue)
            for i in range(level):
                word = queue.popleft()
                tmp = list(word)
                for j in range(len(word)):
                    for l in letters:
                        if l!=word[j]:
                            tmp[j]=l
                            new_word = "".join(tmp)
                            if new_word in wordList:
                                if new_word==endWord:
                                    return step+1
                                if new_word not in visited:
                                    # words[word].append(new_word)
                                    queue.append(new_word)
                                    visited.add(new_word)
                            tmp[j] = word[j]
            step+=1
        return 0

    def ladderLength2(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        """
        双向广度搜索,就是从开始单词和结束单词双向搜索，每次遍历测层次节点数少的一方
        :param beginWord:
        :param endWord:
        :param wordList:
        :return:
        """
        words = set(wordList)
        if endWord not in words:
            return 0

        visited = set()
        visited.add(beginWord)
        visited.add(endWord)

        begin_visited = set()
        begin_visited.add(beginWord)

        end_visited = set()
        end_visited.add(endWord)

        step = 1
        letters = "abcdefghijklmnopqrstuvwxyz"
        while begin_visited and end_visited:
            if len(begin_visited)>len(end_visited):
                begin_visited,end_visited = end_visited,begin_visited

            level_words = set()
            for word in begin_visited:
                tmp = list(word)
                for j in range(len(word)):
                    for l in letters:
                        if l!=word[j]:
                            tmp[j] = l
                            tmp_word = "".join(tmp)
                            if tmp_word in words:
                                if tmp_word in end_visited:
                                    return step + 1
                                if tmp_word not in visited:
                                    level_words.add("".join(tmp))
                                    visited.add("".join(tmp))
                            tmp[j] = word[j]
            begin_visited = level_words
            step+=1
        return 0

    def ladderLength3(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        """
        构建图方法，使用虚拟节点，构建
        :param beginWord:
        :param endWord:
        :param wordList:
        :return:
        """
        words = set(wordList)
        if endWord not in words:
            return 0
        self.num = 0
        word_map = {}
        edage_map = defaultdict(list)
        self.add_edage(beginWord,word_map, edage_map)
        for word in wordList:
            self.add_edage(word,word_map,edage_map)
        dist = [float("inf")]*(self.num+1)
        visited = deque([0])
        end_id = word_map.get(endWord)
        dist[0] = 0
        while visited:
            word_id = visited.popleft()
            if word_id == end_id:
                return dist[word_id] // 2 + 1
            for i in edage_map[word_id]:
                if dist[i]==float("inf"):
                    dist[i] = dist[word_id]+1
                    visited.append(i)
        return 0

    def add_word(self,word,word_map):
        if word not in word_map:
            word_map[word]=self.num
            self.num+=1
        return word_map.get(word)

    def add_edage(self, word, word_map,edage_map):
        self.add_word(word, word_map)
        tmp = list(word)
        for i in range(len(word)):
            tmp[i] = "*"
            tmp_word = "".join(tmp)
            self.add_word(tmp_word,word_map)
            tmp_num = word_map.get(tmp_word)
            edage_map[word_map[word]].append(tmp_num)
            edage_map[tmp_num].append(word_map[word])
            tmp[i] = word[i]

if __name__ == '__main__':
    sol = Solution()
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot","dot","dog","lot","log","cog"]
    print(sol.ladderLength3(beginWord,endWord,wordList))






