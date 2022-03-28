# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-03-28
    FileName   : minArray.py
    Author     : Honghe
    Descreption: 剑指 Offer 11. 旋转数组的最小数字
"""

class Solution(object):
    def minArray(self, numbers):
        """
        :type numbers: List[int]
        :rtype: int
        """
        left = 0
        right = len(numbers)-1

        while left<right:
            middle = (right-left)//2+left
            if numbers[middle]<numbers[right]:
                right = middle
            elif numbers[middle]>numbers[right]:
                left = middle+1
            else:
                # 这一步很关键
                right-=1
        return numbers[left]

if __name__ == '__main__':
    sol = Solution()
    numbers = [3, 1]
    print(sol.minArray(numbers))

