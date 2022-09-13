# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-07-08
    FileName   : lenLongestFibSubseq.py
    Author     : Honghe
    Descreption: 
"""
from typing import List

class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        """
        动态规划
        :param arr:
        :return:
        """
        length = len(arr)
        dp = [[0]*length for _ in range(length)]
        nums = {num:index for index, num in enumerate(arr)}

        for i in range(length):
            for j in range(i-1,0,-1):
                if arr[j]*2<=arr[i]:
                    break

                target = arr[i]-arr[j]
                if target in nums:
                    index = nums.get(target)
                    if index < j:
                        dp[j][i]=max(dp[index][j]+1,3)
        return max([max(i) for i in dp])

if __name__ == '__main__':
    sol = Solution()
    arr = [1, 2, 3, 4, 5, 6, 7, 8]
    print(sol.lenLongestFibSubseq(arr))








