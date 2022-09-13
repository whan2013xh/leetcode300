# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-09-06
    FileName   : trap-0904.py
    Author     : Honghe
    Descreption: 42. 接雨水
"""
from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        """
        单调栈:单调递减栈,每次只计算当前位置与最近的边界存储的水量。这个算是按照高度或者说行来计算水量。
        :param height:
        :return:
        """
        if len(height)<=2:
            return 0
        length = len(height)
        stack = []
        res = 0
        if height[0]>0:
            stack.append((height[0],0))
        for i in range(1,length):
            if not stack or height[i]<stack[-1][0]:
                stack.append((height[i],i))
            elif height[i]>=stack[-1][0]:
                while stack:
                    pre,pos = stack.pop()
                    if not stack:
                        break
                    tmp_height = min(stack[-1][0],height[i])
                    tmp_width = i-stack[-1][1]-1
                    res += (tmp_height-pre)*tmp_width
                    if stack[-1][0]>height[i]:
                        break
                stack.append((height[i],i))
        return res

    def trap2(self, height: List[int]) -> int:
        """
        动态规划：这道题的核心还是如何找到左右边界。动态规划的思想是，记录下每个元素对应的左右边界。
        计算的核心依据是计算每个位置能够存储的数量，算是按列来计算。
        :param height:
        :return:
        """
        if len(height)<=2:
            return 0
        left_max = list(range(len(height)))
        right_max = list(range(len(height)))
        for i in range(1,len(height)):
            left_max[i] = left_max[i] if height[left_max[i]]>height[left_max[i-1]] else left_max[i-1]

        for i in range(len(height)-2,-1,-1):
            right_max[i] = right_max[i] if height[right_max[i]]>height[right_max[i+1]] else right_max[i+1]

        res = 0
        for i in range(len(height)):
            res += min(height[left_max[i]],height[right_max[i]])-height[i]

        return res

    def trap3(self, height):
        """
        双指针法：这个是在上面动态规划的基础上的改进。在遍历每个元素时，实际上关注的重点是左右边界，那么其实不需要用数组来存储，而是靠指针。
        :param height:
        :return:
        """
        if len(height)<=2:
            return 0
        left_max = 0
        right_max = 0
        left = 0
        right = len(height)-1
        res = 0
        for i in range(1,len(height)-1):
            if height[left]<height[right]:
                left_max = max(left_max,height[left])
                if height[left+1]<left_max:
                    res+=left_max-height[left+1]
                left+=1
            else:
                right_max = max(right_max, height[right])
                if height[right-1] < right_max:
                    res += right_max - height[right-1]
                right -= 1

        return res



if __name__ == '__main__':
    sol = Solution()
    height = [0,1,0,2,1,0,1,3,2,1,2,1]
    print(sol.trap3(height))


