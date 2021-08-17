# -*- coding: utf-8 -*-
"""
    CreatedDate: 2021-08-17
    FileName   : findDuplicate.py
    Author     : Honghe
    Descreption: 287. 寻找重复数
"""


class Solution(object):
    def findDuplicate(self, nums):
        """
        暴力法：双层循环遍历,超时
        :type nums: List[int]
        :rtype: int
        """
        for index, i in enumerate(nums[:-1]):
            for j in nums[index + 1:]:
                if i == j:
                    return j
        return 0

    def findDuplicate2(self, nums):
        """
        二分法：这个其实是把二分法的思路倒着来，每次二分的中间值当做target，
        判断整个数组中不大于target的数的个数count和理论上的大小。
        如果1~target没有重复数,那么count<=target
        :param nums:
        :return:
        """
        left = 1
        right = len(nums)-1
        res = -1
        while left<=right:
            count = 0
            mid = (right-left)//2+left
            for i in nums:
                if i<=mid:
                    count+=1
            # 如果没有重复数
            if count<=mid:
                left = mid+1
            else:
                right = mid-1
                res = mid
        return res

    def findDuplicate3(self, nums):
        """
        快慢指针法：这个方法解这个题目其实还借用了一个技巧就是把nums中对应索引的值当做指针移动的步长。
        理解这个后就比较好理解这个思路：
        1、先让快慢指针相遇；
        2、找到相遇点就是重复的数字；
        :param nums:
        :return:
        """
        slow = 0
        fast = 0
        while slow!=fast or slow==0:
            slow = nums[slow]
            fast = nums[nums[fast]]
        fast = 0
        while slow!=fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow


if __name__ == '__main__':
    nums = [1, 3, 4, 2, 2]
    sol = Solution()
    res = sol.findDuplicate3(nums)
    print(res)
