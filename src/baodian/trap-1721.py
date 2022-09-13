# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-08-09
    FileName   : trap-1721.py
    Author     : Honghe
    Descreption: 
"""
from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        """
        单调栈：单调递减栈，记录左右大于当前元素的索引
        1、遍历数组，当前元素cur大于递减栈的栈首元素i的时候，弹出该元素i，那么当前栈顶元素j就是左边离元素i最近的大于i的，有j>i and cur>i
        2、计算元素i可以存储的雨量，高度是：min(height[j],height[cur])-height[i]，宽度是 cur-j-1
        3、遍历递归栈，直到栈为空或者有元素大于cur
        4、插入当前元素cur
        5、重复上面动作直到数组遍历完
        :param height:
        :return:
        """
        if len(height)<=2:
            return 0
        min_stack = []
        res = 0

        for i in range(len(height)):
            cur = height[i]
            while min_stack and cur>height[min_stack[-1]]:
                tmp = min_stack.pop()
                if not min_stack:
                    break
                left = min_stack[-1]
                tmp_height = min(height[left],cur)-height[tmp]
                res += tmp_height*(i-left-1)
            min_stack.append(i)
        return res

    def trap2(self, height: List[int]) -> int:
        """
        动态规划：找到每个元素左右最高的高度，然后计算当前元素应该存多少水。
        这里应用动态规划 left[i] = max(left[i],i)
        :param height:
        :return:
        """
        if len(height)<=2:
            return 0
        res = 0
        left = list(range(len(height)))
        right = list(range(len(height)))
        for i in range(1,len(height)):
            if height[i]<height[left[i-1]]:
                left[i] = left[i-1]

        for i in range(len(height)-2,-1,-1):
            if height[i]<height[right[i+1]]:
                right[i] = right[i+1]

        for i in range(1,len(height)):
            res+=min(height[left[i]],height[right[i]])-height[i]
        return res

    def trap3(self, height: List[int]) -> int:
        """
        双指针：这个是在动态规划的基础上改进而来的
        在动态规划中求和时，只关心左右边界的最小值，那么是不是可以将左右边界这个数组压缩为单个变量来记录左右两边的极值
        记左右指针分别为left,right,左边最大的为left_max,右边为right_max
        这里需要注意的是left和right啥时候移动，只有height[left]<height[right]时left才向右移动，
        因为我们计算的核心逻辑还是不变的，那就是找左右两边的高点，只有当height[left]<height[right]时，那么在left的位置可以存放的雨量就是
        left_max-height[left]。对应right同理。
        :param height:
        :return:
        """
        if len(height)<=2:
            return 0
        res = 0
        left = 0
        right = len(height)-1
        left_max=0
        right_max = 0
        while left<right:
            left_max = max(left_max, height[left])
            right_max = max(right_max, height[right])
            if height[left]<height[right]:
                res+=left_max-height[left]
                left+=1
            else:
                res += right_max - height[right]
                right-=1
        return res


if __name__ == '__main__':
    sol = Solution()
    height = [2,0,2]
    print(sol.trap3(height))





