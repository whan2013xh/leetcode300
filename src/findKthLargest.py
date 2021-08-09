# -*- coding: utf-8 -*-
"""
    CreatedDate: 2021-08-09
    FileName   : findKthLargest.py
    Author     : Honghe
    Descreption: 215. 数组中的第K个最大元素
"""


class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        self.quick_sort2(nums, 0, len(nums) - 1)
        return nums[-k]

    def quick_sort(self, nums, start, end):
        """
        快速排序双指针法：需要注意的是如果选择左边第一个节点为基础值得话，那么要右边的指针先移动，
        否则会出现问题，因为左边先动无法保证跳出循环时左指针所指向的值就一点大于基础值
        :param nums:
        :param start:
        :param end:
        :return:
        """
        if start >= end:
            return
        left = start
        right = end
        base = nums[left]
        while start < end:
            while start < end and nums[end] > base:
                end -= 1
            while start < end and nums[start] <= base:
                start += 1

            if start < end:
                nums[start], nums[end] = nums[end], nums[start]
        nums[left], nums[start] = nums[start], nums[left]
        self.quick_sort(nums, left, start - 1)
        self.quick_sort(nums, start + 1, right)

    def quick_sort2(self, nums, start, end):
        """
        快速排序单指针法：选择右边节点为基础节点，遍历整个数组，把小于基础节点的都放到左边
        :param nums:
        :param start:
        :param end:
        :return:
        """
        if start >= end:
            return
        left = start - 1
        base = nums[end]
        if start < end:
            for i in range(start, end):
                if nums[i] < base:
                    left += 1
                    nums[left], nums[i] = nums[i], nums[left]
            nums[left + 1], nums[end] = nums[end], nums[left + 1]
            self.quick_sort2(nums, start, left)
            self.quick_sort2(nums, left + 2, end)


if __name__ == '__main__':
    nums = [2, 1]
    k = 1
    sol = Solution()
    res = sol.findKthLargest(nums, k)
    print(nums)
    print(res)
