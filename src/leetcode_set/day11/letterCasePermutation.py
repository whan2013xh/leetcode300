# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-03-21
    FileName   : letterCasePermutation.py
    Author     : Honghe
    Descreption: 784. 字母大小写全排列
"""
import copy

class Solution(object):
    def letterCasePermutation(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        words = list(s)
        res = []
        tmp_words = []
        tmp_index = []
        for index,word in enumerate(words):
            if not word.isdigit():
               tmp_words.append(word)
               tmp_index.append(index)
        self.dfs(tmp_words,res,[],len(tmp_words))
        new_words = []
        for word in res:
            for index,i in enumerate(tmp_index):
                words[i] = word[index]
            new_words.append("".join(words))
        return new_words

    def dfs(self, words, res,tmp_list,word_length):
        if len(tmp_list)==word_length and tmp_list not in res:
            res.append(copy.deepcopy(tmp_list))
            return
        for index,word in enumerate(words):
            tmp_list.append(word.lower())
            self.dfs(words[index+1:], res,tmp_list,word_length)
            tmp_list.pop()
            tmp_list.append(word.upper())
            self.dfs(words[index+1:], res, tmp_list,word_length)
            tmp_list.pop()


if __name__ == '__main__':
    sol = Solution()
    s = "a1b2c3"
    print(sol.letterCasePermutation(s))

