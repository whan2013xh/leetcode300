# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-06-02
    FileName   : canPartition-0602.py
    Author     : Honghe
    Descreption: 416. 分割等和子集
"""

class Solution(object):
    def canPartition(self, nums):
        """
        递归解法，会超时
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums)<2 or sum(nums)%2!=0:
            return False
        target = sum(nums)//2
        res_nums = []
        visited = {}
        return self.dp(nums,target,res_nums,visited)


    def dp(self,nums,target,res_nums,visited):
        if target==0 and res_nums:
            return True
        if visited.get(target,False):
            return True
        for index,num in enumerate(nums):
            visited[target] = self.dp(nums[index+1:],target,res_nums,visited)|self.dp(nums[index+1:],target-num,res_nums+[num],visited)
            return visited[target]
        return False

    def canPartition2(self, nums):
        """
        子集背包解法
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums)<2 or sum(nums)%2!=0:
            return False
        max_num = max(nums)
        target = sum(nums) // 2
        if max_num>target:
            return False

        dp = [[False]*(target+1) for _ in range(len(nums)+1)]
        for i in range(len(nums)+1):
            dp[i][0] = True
        for i in range(1,len(nums)+1):
            num = nums[i-1]
            for j in range(1,target+1):
                if num<=j:
                   dp[i][j] = dp[i-1][j-num]|dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[-1][-1]


if __name__ == '__main__':
    sol =Solution()
    nums = [2,2,3,5]
    print(sol.canPartition2(nums))