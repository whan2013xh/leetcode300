# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-03-10
    FileName   : sortedSquares.py
    Author     : Honghe
    Descreption: 977. 有序数组的平方
"""

class Solution(object):
    def sortedSquares(self, nums):
        """
        算法复杂了，可以简化
        1、先找到非负数的索引；
        2、两个指针遍历
        :type nums: List[int]
        :rtype: List[int]
        """
        square_list = [i*i for i in nums]
        left = 0
        right = len(nums)-1
        middle_pos = -1
        while left<=right:
            middle = (right-left)//2 + left
            if nums[middle]==0:
                middle_pos=middle
                break
            elif nums[middle]<0:
                left = middle+1
            elif nums[middle]>0:
                right = middle-1
        order = True
        if middle_pos==-1:
            if left>len(nums)-1:
                order = False
            elif nums[left]<=0:
                order = False
            else:
                middle_pos = left
        left=0
        if not order:
            return square_list[::-1]
        res = []
        right = len(nums)-1
        while left<middle_pos and right>=middle_pos:
            left_tmp = abs(nums[left])
            if left_tmp>=nums[right]:
                res.append(left_tmp*left_tmp)
                left+=1
            elif left_tmp<nums[right]:
                res.append(nums[right]*nums[right])
                right-=1
        if left==middle_pos:
            res+=[i*i for i in nums[left:right+1]][::-1]
        else:
            res += [i * i for i in nums[left:right+1]]
        return res[::-1]

    def sortedSquares(self, nums):
        """

        :param nums:
        :return:
        """
        left = 0
        right = len(nums)-1
        pos = len(nums)-1
        res = [0]*len(nums)
        while left<=right:
            if nums[left]*nums[left]>=nums[right]*nums[right]:
                res[pos]=nums[left]*nums[left]
                left+=1
            else:
                res[pos] = nums[right] * nums[right]
                right-=1
            pos-=1
        return res

if __name__ == '__main__':
    sol = Solution()
    nums = [-1]
    res = sol.sortedSquares(nums)
    print(res)



