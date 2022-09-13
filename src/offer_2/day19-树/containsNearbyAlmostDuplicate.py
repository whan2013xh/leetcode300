# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-06-27
    FileName   : containsNearbyAlmostDuplicate.py
    Author     : Honghe
    Descreption: 剑指 Offer II 057. 值和下标之差都在给定的范围内
"""
from typing import List

class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        if not nums:
            return False

        num_dict = {}

        for index,num in enumerate(nums):
            num_id = self.get_num_id(num,burket_size=t+1)
            if num_id in num_dict:
                return True
            elif num_id-1 in num_dict and abs(num-num_dict.get(num_id-1))<=t:
                return True
            elif num_id+1 in num_dict and abs(num-num_dict.get(num_id+1))<=t:
                return True
            num_dict[num_id] = num
            if index>=k:
                tmp_id = self.get_num_id(nums[index-k],t+1)
                num_dict.pop(tmp_id)
        return False

    def get_num_id(self, num, burket_size):
        """
        这里说明一下Python3的负数整除
        :param num:
        :param burket_size:
        :return:
        """
        return num//burket_size

    def containsNearbyAlmostDuplicate2(self, nums: List[int], k: int, t: int) -> bool:

        def get_bucket_id(num, bucket_size):
            return ((num + 1) // bucket_size) - 1 if num < 0 else num // bucket_size

        bucket_map = {}
        for i, num in enumerate(nums):
            bucket_id = get_bucket_id(num, t + 1)

            if bucket_id in bucket_map:  # 检查是否有符合条件的元素
                return True
            elif bucket_id - 1 in bucket_map and abs(num - bucket_map[bucket_id - 1]) <= t:
                return True
            elif bucket_id + 1 in bucket_map and abs(num - bucket_map[bucket_id + 1]) <= t:
                return True

            bucket_map[bucket_id] = num  # 添加新桶

            if i - k >= 0:  # 删除超出窗口长度的旧桶
                del_id = get_bucket_id(nums[i - k], t + 1)
                bucket_map.pop(del_id)

        return False




if __name__ == '__main__':
    nums = [1,5,9,2]
    k=2
    t=1
    sol = Solution()
    print(sol.containsNearbyAlmostDuplicate(nums,k,t))