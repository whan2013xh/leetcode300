# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-04-24
    FileName   : numberOfArithmeticSlices.py
    Author     : Honghe
    Descreption: 413. 等差数列划分
"""
class Solution(object):
    def numberOfArithmeticSlices(self, nums):
        """
        暴力法
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)<=2:
            return 0
        res = []
        for i in range(1,len(nums)):
            step = nums[i]-nums[i-1]
            for j in range(i+1,len(nums)):
                if nums[j]-nums[i]==(j-i)*step:
                    res.append(nums[i-1:j+1])
                else:
                    break
        print(res)
        return len(res)

    def numberOfArithmeticSlices2(self, nums):
        """
        暴力法
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)<=2:
            return 0
        res = 0
        i=1
        while i<len(nums)-1:
            step = nums[i]-nums[i-1]
            tmp = 0
            for j in range(i+1,len(nums)):
                if nums[j]-nums[i]==(j-i)*step:
                    tmp = 1 if tmp==0 else tmp+j-i
                    if j==len(nums)-1:
                        res += tmp
                        i = j
                        break
                else:
                    res+=tmp
                    i = j
                    break
        return res

    def numberOfArithmeticSlices3(self, nums):
        count = 0
        dp = [0]*len(nums)
        for i in range(2,len(nums)):
            if nums[i]-nums[i-1]==nums[i-1]-nums[i-2]:
                dp[i]=dp[i-1]+1
                count+=dp[i]

        return count



if __name__ == '__main__':
    sol = Solution()
    nums = [1,2,3,4,5,6]
    print(sol.numberOfArithmeticSlices2(nums))
