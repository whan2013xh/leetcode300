# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-03-11
    FileName   : twoSum.py
    Author     : Honghe
    Descreption: 
"""


class Solution(object):
    def twoSum(self, numbers, target):
        """
        二分法
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        for index, value in enumerate(numbers):
            if value > target // 2:
                return
            left = index + 1
            right = len(numbers) - 1
            other_value = target - value
            while left <= right:
                middle = (right - left) // 2 + left
                if numbers[middle] > other_value:
                    right = middle - 1
                elif numbers[middle] < other_value:
                    left = middle + 1
                else:
                    return [index + 1, middle + 1]

    def twoSum2(self, numbers, target):
        """

        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        left = 0
        right = len(numbers) - 1
        while left < right:
            if numbers[left] + numbers[right] == target:
                return [left + 1, right + 1]
            elif numbers[left] + numbers[right] < target:
                left += 1
            else:
                right -= 1
        return [-1, -1]


if __name__ == '__main__':
    sol = Solution()
    numbers = [-1, 0]
    target = -1
    res = sol.twoSum2(numbers, target)
    print(res)
