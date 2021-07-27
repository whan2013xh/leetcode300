# -*- coding: utf-8 -*-
"""
    CreatedDate: 2021-07-27
    FileName   : majorityElement.py
    Author     : Honghe
    Descreption: 169. 多数元素
"""

class Solution(object):
    def majorityElement(self, nums):
        """
        排序法：这个方法应该是最容易想到的，排序后取中间元素即可
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        return nums[len(nums)//2]

    def majorityElement2(self, nums):
        """
        hash法：就是遍历数组，统计出现次数最多的，空间复杂度高
        :param nums:
        :return:
        """
        count = {}
        for num in nums:
            count[num] = count.get(num, 0)+1

        for key,value in count.items():
            if value>len(nums)//2:
                return key

    def majorityElement3(self, nums):
        """
        分治法
        :param nums:
        :return:
        """
        return self.get_majority(nums, 0, len(nums)-1)

    def get_majority(self, nums, left, right):
        if left==right:
            return nums[left]

        mid = left + (right-left)//2
        left_majority = self.get_majority(nums, left, mid)
        right_majority = self.get_majority(nums, mid+1, right)
        if left_majority==right_majority:
            return left_majority
        left_count=0
        right_count=0
        for i in range(left, right+1):
            if nums[i]==left_majority:
                left_count+=1
            if nums[i]==right_majority:
                right_count+=1
        return left_majority if left_count>right_count else right_majority

    def majorityElement4(self, nums):
        """
        摩尔投票法：众数的特征是出现次数大于len(nums)/2，那么我们把不等于这个众数的分为一类，众数分为一类
        假设众数是第一个元素，当等于众数时记为1，不等记为-1，每次累加的和为count，当count为0的时候把众数改成下一位元素
        :param nums:
        :return:
        """
        count = 0
        majority = None
        for num in nums:
            if count==0:
                majority = num
            count += 1 if num==majority else -1
        return majority

if __name__ == '__main__':
    nums = [3,2,3]
    sol = Solution()
    res = sol.majorityElement3(nums)
    print(res)