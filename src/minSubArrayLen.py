# -*- coding: utf-8 -*-
"""
    CreatedDate: 2021-08-02
    FileName   : minSubArrayLen.py
    Author     : Honghe
    Descreption: 209. 长度最小的子数组
"""


class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        暴力法：
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        res = len(nums) + 1
        for i in range(len(nums)):
            total = nums[i]
            if total >= target:
                res = 1
                break
            else:
                for j in range(i + 1, len(nums)):
                    total += nums[j]
                    if total >= target:
                        res = min(res, j - i + 1)
                        break
        return 0 if res == len(nums) + 1 else res

    def minSubArrayLen2(self, target, nums):
        """
        滑动窗口法：维护一前一后两个指针，指针间的距离是窗口长度
        当窗口内元素和小于target的是，窗口右指针向右滑动
        当小于target的时候，窗口左指针向右滑动
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        res = len(nums) + 1
        i = 0

        while i < len(nums):
            j = i
            while i <= j and j <= len(nums) - 1:
                total = sum(nums[i:j + 1])
                if total < target:
                    j += 1
                else:
                    res = min(res, j - i + 1)
                    i += 1
            if j > len(nums) - 1:
                break
        return 0 if res == len(nums) + 1 else res


if __name__ == '__main__':
    target = 213
    nums = [12, 28, 83, 4, 25, 26, 25, 2, 25, 25, 25, 12]
    sol = Solution()
    res = sol.minSubArrayLen2(target, nums)
    print(res)
