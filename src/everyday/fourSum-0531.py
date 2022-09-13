# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-05-31
    FileName   : fourSum-0531.py
    Author     : Honghe
    Descreption: 18. 四数之和
"""

class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if len(nums)<4:
            return []

        nums.sort()
        res = []
        for index,num in enumerate(nums[:-3]):
            # if num>target:
            #     break
            for index2,num2 in enumerate(nums[index+1:-2]):
                # if num2>target-num:
                #     break
                left = index2+index+1+1
                right = len(nums)-1
                while left<right:
                    if nums[left]+nums[right]>target-num-num2:
                        right-=1
                    elif nums[left]+nums[right]<target-num-num2:
                        left+=1
                    else:
                        res.append([num,num2,nums[left],nums[right]])
                        left+=1
                        right-=1
                        while left<right and nums[left]==nums[left-1]:
                            left+=1
                        while left<right and nums[right]==nums[right+1]:
                            right-=1

        return res

if __name__ == '__main__':
    sol = Solution()
    nums = [1,-2,-5,-4,-3,3,3,5]
    target = -11
    print(sol.fourSum(nums,target))

