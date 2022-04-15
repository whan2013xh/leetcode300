# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-04-07
    FileName   : findPeakElement.py
    Author     : Honghe
    Descreption: 162. 寻找峰值
"""
class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        tmp = float("-inf")
        nums = [tmp]+nums+[tmp]
        return self.binary_search(nums)-1

    def binary_search(self, nums):
        left = 0
        right = len(nums) - 1
        middle = (right-left)//2+left
        if nums[middle-1]<nums[middle]and nums[middle]>nums[middle+1]:
            return middle
        else:
            if middle-left<=1:
                for i in range(left+1,right):
                    if nums[i-1]<nums[i] and nums[i]>nums[i+1]:
                        return i
                return None
            left_res = self.binary_search(nums[left:middle+1])
            if left_res is not None:
                return left+left_res

            right_res = self.binary_search(nums[middle:right+1])
            if right_res is not None:
                return middle+right_res

    def findPeakElement2(self, nums):
        n = len(nums)

        # 辅助函数，输入下标 i，返回 nums[i] 的值
        # 方便处理 nums[-1] 以及 nums[n] 的边界情况
        def get(i: int) -> int:
            if i == -1 or i == n:
                return float('-inf')
            return nums[i]

        left, right, ans = 0, n - 1, -1
        while left <= right:
            mid = (left + right) // 2
            if get(mid - 1) < get(mid) > get(mid + 1):
                ans = mid
                break
            if get(mid) < get(mid + 1):
                left = mid + 1
            else:
                right = mid - 1

        return ans

if __name__ == '__main__':
    sol = Solution()
    nums = [1,2,3,1]
    print(sol.findPeakElement(nums))
