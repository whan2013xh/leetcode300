# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-04-19
    FileName   : letterCombinations.py
    Author     : Honghe
    Descreption: 17. 电话号码的字母组合
"""

class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
        words = ['abc','def','ghi','jkl','mno','pqrs','tuv','wxyz']
        words_list = []
        res = []
        for i in digits:
            index = int(i)-2
            words_list.append(words[index])
        self.back_trace(words_list,res,[],0)
        return res


    def back_trace(self,words_list,res,tmp,begin):
        if len(tmp)==len(words_list):
            res.append("".join(tmp))
            return
        for index,word in enumerate(words_list[begin:]):
            for letter in word:
                tmp.append(letter)
                self.back_trace(words_list,res,tmp,index+begin+1)
                tmp.pop()


if __name__ == '__main__':
    sol = Solution()
    digits = "234"
    print(sol.letterCombinations(digits))




