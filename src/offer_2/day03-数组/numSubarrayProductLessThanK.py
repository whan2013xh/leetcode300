# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-05-09
    FileName   : numSubarrayProductLessThanK.py
    Author     : Honghe
    Descreption: 剑指 Offer II 009. 乘积小于 K 的子数组
"""


class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if not nums:
            return 0
        if len(nums)==1:
            return 1 if nums[0]<k else 0
        left = len(nums)
        res = 1
        res_list = []
        for index,num in enumerate(nums):
            res *=num

            if res>=k:
                if left!=len(nums):
                    res_list.append((left,index-1))
                    while left<=index:
                        res/=nums[left]
                        left += 1
                        if res<k:
                            break
                    if left>index:
                        left = len(nums)
                    if index == len(nums) - 1 and res<k:
                        res_list.append((left, index))
                else:
                    res/=num
            else:
                if left==len(nums):
                    left = index
                if index==len(nums)-1:
                    res_list.append((left, index))
        result = 0
        pre_left = -1
        pre_right = -1
        for left,right in res_list:
            if pre_left<0 or left>pre_right:
                repeat_times = 0
            else:
                repeat_times = (pre_right-left+1+1)*(pre_right-left+1)/2
            pre_left = left
            pre_right = right

            result += (right-left+1+1)*(right-left+1)/2-repeat_times
        return int(result)

    def numSubarrayProductLessThanK2(self, nums, k):
        """
        滑动窗口法：窗口以右边窗口固定，每次计算包含右边窗口的数新增的组合个数
        :type nums: List[int]
        :type k: int
        :rty
        """
        result = 0
        left = 0
        res = 1
        for index,num in enumerate(nums):
            res*=num
            while left<=index and res>=k:
                res/=nums[left]
                left+=1
            result += index-left+1
        return result

if __name__ == '__main__':
    sol = Solution()
    nums = [10,9,10,4,3,8,3,3,6,2,10,10,9,3]
    k = 19
    print(sol.numSubarrayProductLessThanK(nums,k))





