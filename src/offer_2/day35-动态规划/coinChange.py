# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-07-13
    FileName   : coinChange.py
    Author     : Honghe
    Descreption: 322. 零钱兑换
"""
from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        length = len(coins)
        dp = [[float("inf")]*(length+1) for _ in range(amount+1)]
        for i in range(amount+1):
            for j in range(length+1):
                if i==0:
                    dp[i][j]=0
                    continue
                if j==0:
                    continue
                if coins[j-1]==i:
                   dp[i][j] = 1
                elif coins[j-1]<i:
                    dp[i][j] = min(dp[i][j-1],dp[i-coins[j-1]][j]+1)
                else:
                    dp[i][j] = dp[i][j-1]
        return dp[-1][-1] if dp[-1][-1]!=float("inf") else -1

    def coinChange2(self, coins: List[int], amount: int) -> int:
        dp = [float("inf")]*(amount+1)
        dp[0] = 0
        for i in range(1,amount+1):
            for j in coins:
                if i>=j:
                    dp[i] = min(dp[i],dp[i-j]+1)
        return dp[-1] if dp[-1]!=float("inf") else -1

if __name__ == '__main__':
    sol = Solution()
    coins = [5,1,2]
    amount = 11
    print(sol.coinChange2(coins,amount))

