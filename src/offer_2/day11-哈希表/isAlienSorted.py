# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-06-16
    FileName   : isAlienSorted.py
    Author     : Honghe
    Descreption: 
"""

class Solution(object):
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        if len(words)==1:
            return True
        alien_order = {}
        for index,i in enumerate(order):
            alien_order[i] = index

        for index,word in enumerate(words[:-1]):
            res = self.is_big(word,words[index+1],alien_order)
            if not res:
                return False
        return True

    def is_big(self, word1, word2, alien_order):
        for index,letter1 in enumerate(word1):
            if index>len(word2)-1 or alien_order[letter1]>alien_order[word2[index]]:
                return False
            if alien_order[letter1]<alien_order[word2[index]]:
                return True
        return True

if __name__ == '__main__':
    sol =Solution()
    words = ["hello","hello"]
    order = "abcdefghijklmnopqrstuvwxyz"
    print(sol.isAlienSorted(words,order))


