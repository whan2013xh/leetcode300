# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-04-07
    FileName   : isStraight.py
    Author     : Honghe
    Descreption: 剑指 Offer 61. 扑克牌中的顺子
"""

class Solution(object):
    def isStraight(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        repeat = set()
        ma, mi = 0, 14
        for num in nums:
            if num == 0: continue  # 跳过大小王
            ma = max(ma, num)  # 最大牌
            mi = min(mi, num)  # 最小牌
            if num in repeat: return False  # 若有重复，提前返回 false
            repeat.add(num)  # 添加牌至 Set
        return ma - mi < 5

