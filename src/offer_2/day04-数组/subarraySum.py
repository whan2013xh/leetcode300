# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-05-16
    FileName   : subarraySum.py
    Author     : Honghe
    Descreption: 剑指 Offer II 010. 和为 k 的子数组
"""

class Solution(object):
    def subarraySum(self, nums, k):
        """
        暴力法
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        target = 0
        res = 0
        for index,num in enumerate(nums):
            target+=num
            left = 0
            if target==k:
                res+=1
            tmp = target
            while left<index:
                tmp-=nums[left]
                if tmp==k:
                    res+=1
                left+=1
        return res

    def subarraySum2(self, nums, k):
        presum = 0  # 前缀和
        dic = {0: 1}  # dic[key]:value,代表前缀和key出现的次数
        ans = 0
        for num in nums:
            presum += num
            # presum - target 表示以起始点到当前num为终点的前缀和比target多出的距离
            ans += dic.get(presum - k, 0)
            dic[presum] = dic.get(presum, 0) + 1
        return ans

    def subarraySum3(self, nums, k):
        sum_num = 0
        sum_dict={}
        res = 0
        for index,num in enumerate(nums):
            sum_num += num
            res += sum_dict.get(sum_num-k,0)
            sum_dict[sum_num] = sum_dict.get(sum_num,0)+1
        return res

if __name__ == '__main__':
    sol =Solution()
    nums = [1, 1, 1 ]
    k = 2
    print(sol.subarraySum(nums,k))

