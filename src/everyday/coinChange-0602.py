# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-06-02
    FileName   : coinChange.py
    Author     : Honghe
    Descreption: 322. 零钱兑换
"""

class Solution(object):
    def coinChange(self, coins, amount):
        """
        无限背包问题
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp = [[amount+1]*(amount+1) for _ in range(len(coins)+1)]
        for i in range(len(coins)+1):
            dp[i][0] = 0

        for i in range(1,len(coins)+1):
            coin = coins[i-1]
            for j in range(1,amount+1):
                if j>=coin:
                    dp[i][j] = min(dp[i-1][j],dp[i-1][j-coin]+1,dp[i][j-coin]+1)
                else:
                    dp[i][j] = dp[i-1][j]
        return -1 if dp[-1][-1]==amount+1 else dp[-1][-1]


if __name__ == '__main__':
    sol = Solution()
    coins = [1]
    amount = 0
    print(sol.coinChange(coins,amount))

