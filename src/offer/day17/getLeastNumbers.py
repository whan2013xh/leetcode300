# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-04-07
    FileName   : getLeastNumbers.py
    Author     : Honghe
    Descreption: 剑指 Offer 40. 最小的k个数
"""

class Solution(object):
    def getLeastNumbers(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: List[int]
        """
        for index,num in enumerate(arr):
            tmp = num
            for j in range(index+1,len(arr)):
                if tmp>arr[j]:
                    tmp,arr[j] = arr[j],tmp
            arr[index]=tmp
        return arr[:k]

if __name__ == '__main__':
    sol = Solution()
    arr = [3,2,1]
    k=2
    print(sol.getLeastNumbers(arr,k))



