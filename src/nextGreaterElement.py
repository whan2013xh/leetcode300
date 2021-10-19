# -*- coding: utf-8 -*-
"""
    CreatedDate: 2021-10-19
    FileName   : nextGreaterElement.py
    Author     : Honghe
    Descreption: 496. 下一个更大元素 I
"""

class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        哈希法：先遍历nums2找到对应每个元素的最大值，然后再遍历nums1即可
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        visit_nums = []
        hash_nums = {}
        for i in nums2:
            if not visit_nums or i<visit_nums[-1]:
                visit_nums.append(i)
                continue
            while visit_nums and i>visit_nums[-1]:
                tmp = visit_nums.pop(-1)
                hash_nums[tmp] = i
            visit_nums.append(i)
        return [hash_nums.get(i,-1) for i in nums1]

if __name__ == '__main__':
    nums1 = [4,1,2]
    nums2 = [1, 3, 4, 2]
    sol = Solution()
    res = sol.nextGreaterElement(nums1,nums2)
    print(res)