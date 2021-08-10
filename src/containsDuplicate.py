# -*- coding: utf-8 -*-
"""
    CreatedDate: 2021-08-10
    FileName   : containsDuplicate.py
    Author     : Honghe
    Descreption: 217. 存在重复元素
"""
class Solution(object):
    def containsDuplicate(self, nums):
        """
        去重法：直接比较set前后数组长度即可
        :type nums: List[int]
        :rtype: bool
        """
        return len(nums)>len(set(nums))

    def containsDuplicate2(self, nums):
        """
        排序法
        :param nums:
        :return:
        """
        nums.sort()
        prev = nums[0]
        for i in nums[1:]:
            if prev==i:
                return True
            prev = i
        return False


if __name__ == '__main__':
    nums = [1,2,3,1]
    sol = Solution()
    res = sol.containsDuplicate2(nums)
    print(res)