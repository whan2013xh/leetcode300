# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-08-22
    FileName   : oneEditAway-0105.py
    Author     : Honghe
    Descreption: 
"""

class Solution:
    def oneEditAway(self, first: str, second: str) -> bool:
        if first==second:
            return True
        m = len(first)
        n = len(second)
        if abs(m-n)>=2:
            return False

        if m>n:
            return self.oneEditAway(second,first)
        for i in range(m):
            if first[i]!=second[i]:
                return first[i:]==second[i+1:] if m<n else first[i+1:]==second[i+1:]
        return True


if __name__ == '__main__':
    sol = Solution()
    first = "pale"
    second = "pala"
    print(sol.oneEditAway(first,second))
