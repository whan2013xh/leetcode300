# -*- coding: utf-8 -*-
"""
    CreatedDate: 2021-08-09
    FileName   : findKthLargest.py
    Author     : Honghe
    Descreption: 
"""
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        self.quick_sort(nums, 0, len(nums)-1)
        return nums[-k]


    def quick_sort(self, nums, start, end):
        if start>=end:
            return
        left = start
        right = end
        base = nums[left]
        # start+=1
        while start<end:
            while start<=end and nums[start]<=base:
                start+=1
            while start<=end and nums[end]>base:
                end-=1
            if start<end:
                nums[start], nums[end] = nums[end], nums[start]
        nums.insert(start, base)
        nums.pop(left)
        self.quick_sort(nums, left, start-1)
        self.quick_sort(nums, start, right)


if __name__ == '__main__':
    nums = [3,2,1,5,6,4]
    k = 2
    sol = Solution()
    res = sol.findKthLargest(nums, k)
    print(nums)
    print(res)