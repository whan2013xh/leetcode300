# -*- coding: utf-8 -*-
"""
    CreatedDate: 2021-08-23
    FileName   : removeElement.py
    Author     : Honghe
    Descreption: 27. 移除元素
"""

class Solution(object):
    def removeElement(self, nums, val):
        """
        直接遍历
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        val_index = 0
        for index, i in enumerate(nums):
            if i != val:
                nums[val_index] = i
                val_index += 1
        nums = nums[:val_index]
        return val_index

    def removeElement2(self, nums, val):
        """
        双指针法：
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        left = 0
        right = len(nums)-1
        while left<right:
            while nums[right]==val and left<right:
                right-=1
            while nums[left]!=val and left<right:
                left+=1
            nums[left],nums[right]=nums[right], nums[left]

        if nums[left]!=val:
            left +=1
        nums = nums[:left]
        print(nums)
        return left

if __name__ == '__main__':
    nums = [1]
    val = 1
    sol = Solution()
    res = sol.removeElement2(nums, val)

    print(res)