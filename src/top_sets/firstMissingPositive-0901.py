# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-09-02
    FileName   : firstMissingPositive-0901.py
    Author     : Honghe
    Descreption: 
"""
from typing import List

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        """
        置换法：数组长度n,那么nums要么是[1,n]的集合，那么对应的最小值是n+1
        要么最小值在[1,n]内，把元素排序交换到对应索引的位置，注意两个元素相等的问题
        :param nums:
        :return:
        """
        if not nums:
            return 1

        length = len(nums)
        for index,num in enumerate(nums):
            while length>=num>0:
                if num==nums[num-1]:
                    break
                nums[index],nums[num-1]=nums[num-1],nums[index]
                num = nums[index]

        for index,num in enumerate(nums):
            if num!=index+1:
                return index+1
        return length+1

    def firstMissingPositive2(self, nums: List[int]) -> int:
        """
        哈希法：数组长度n,那么nums要么是[1,n]的集合，那么对应的最小值是n+1
        要么最小值在[1,n]内，那么维护一个key为1~n的哈希表，对应的value是索引值。
        但是要求空间复杂度是O(1)，那么考虑借助nums本身来实现。
        1、遍历数组，把负数转成N+1
        2、遍历数组，把对应value对应的索引位置置为负数
        3、遍历数组，找到最小的那个索引位置
        :param nums:
        :return:
        """
        length = len(nums)
        for index,num in enumerate(nums):
            if num<=0:
                nums[index] = length+1

        for index,num in enumerate(nums):
            tmp = abs(num)
            if 0<tmp<=length:
                nums[tmp-1] = -abs(nums[tmp-1])

        for index,num in enumerate(nums):
            if num>0:
                return index+1
        return length+1


if __name__ == '__main__':
    sol = Solution()
    nums = [3,4,-1,1]
    print(sol.firstMissingPositive2(nums))




