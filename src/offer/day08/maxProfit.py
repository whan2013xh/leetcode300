# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-03-30
    FileName   : maxProfit.py
    Author     : Honghe
    Descreption: 剑指 Offer 63. 股票的最大利润
"""

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        cost = float("+inf")
        profit = 0
        for i in prices:
            cost = min(cost,i)
            profit = max(profit,i-cost)
        return profit



if __name__ == '__main__':
    sol = Solution()
    prices = [7,1,5,3,6,4]
    print(sol.maxProfit(prices))

