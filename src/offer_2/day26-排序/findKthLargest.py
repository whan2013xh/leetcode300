# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-07-04
    FileName   : findKthLargest.py
    Author     : Honghe
    Descreption: 
"""
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return self.heap_sort(nums,k)

    def heapfy(self,nums, index):
        child = 2 * index + 1
        size = len(nums)
        while child < size:
            if child + 1 < size and nums[child] < nums[child + 1]:
                child += 1
            if nums[index] < nums[child]:
                nums[index], nums[child] = nums[child], nums[index]
                index = child
                child = 2 * index + 1
            else:
                break

    def heap_sort(self, nums,k):
        for i in range(len(nums)//2,-1,-1):
            self.heapfy(nums,i)

        for i in range(len(nums)-1,len(nums)-k,-1):
            nums[0],nums[-1] = nums[-1],nums[0]
            nums.pop()
            self.heapfy(nums,0)
        return nums[0]


if __name__ == '__main__':
    sol = Solution()
    n = [3, 2, 3, 1, 2, 4, 5, 5, 6]
    k = 4
    print(sol.findKthLargest(n,k))


