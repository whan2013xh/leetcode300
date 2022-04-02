# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-04-01
    FileName   : canReorderDoubled-0401.py
    Author     : Honghe
    Descreption: 954. 二倍数对数组
"""

class Solution:
    def canReorderDoubled(self, arr):
        arr.sort()
        target = []
        for i in arr:
            if i<=0:
                if i not in target:
                    if i%2!=0:
                        return False
                    target.append(i//2)
                else:
                    target.remove(i)
            else:
                if i not in target:
                    target.append(i*2)
                else:
                    target.remove(i)
        return len(target)==0

if __name__ == '__main__':
    sol = Solution()
    arr = [2,4,0,0,8,1]
    print(sol.canReorderDoubled(arr))
