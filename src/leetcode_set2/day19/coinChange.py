# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-04-26
    FileName   : coinChange.py
    Author     : Honghe
    Descreption: 322. 零钱兑换
"""

class Solution(object):
    def coinChange(self, coins, amount):
        """
        背包问题
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp = [float("inf")]*(amount+1)
        dp[0]=0
        for i in range(1,len(coins)+1):
            for j in range(coins[i-1],amount+1):
                dp[j] = min(dp[j],dp[j-coins[i-1]]+1)
        return -1 if dp[-1]==float("inf") else dp[-1]

if __name__ == '__main__':
    sol = Solution()
    coins = [2]
    amount = 3
    print(sol.coinChange(coins,amount))
