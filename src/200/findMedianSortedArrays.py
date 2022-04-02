# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-03-31
    FileName   : findMedianSortedArrays.py
    Author     : Honghe
    Descreption: 4. 寻找两个正序数组的中位数
"""

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        length1 = len(nums1)
        length2 = len(nums2)
        flag = (length1+length2)%2==0
        middle = (length1+length2)//2
        if length1==0:
            if flag:
                return (nums2[middle-1]+nums2[middle])/2
            else:
                return nums2[middle]
        elif length2==0:
            if flag:
                return (nums1[middle-1]+nums1[middle])/2
            else:
                return nums1[middle]
        pos1 = 0
        pos2 = 0
        count1 = 0
        count2 = 0
        count=0
        res = []
        while count<=middle:
            if nums1[pos1]>=nums2[pos2]:
                if count2>length2-1:
                    tmp = nums1[pos1]
                    pos1+=1
                else:
                    tmp = nums2[pos2]
                    pos2 = min(pos2+1,length2-1)
                    count2+=1
            elif nums1[pos1]<nums2[pos2]:
                if count1 > length1 - 1:
                    tmp = nums2[pos2]
                    pos2+=1
                else:
                    tmp = nums1[pos1]
                    pos1 = min(pos1+1,length1-1)
                    count1+=1
            if count>=middle-1:
                res.append(tmp)
            count+=1
        return sum(res)/2 if flag else max(res)

if __name__ == '__main__':
    sol = Solution()
    nums1 = [1,2]
    nums2 = [3,4]
    print(sol.findMedianSortedArrays(nums1,nums2))






