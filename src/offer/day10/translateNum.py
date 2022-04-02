# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-03-31
    FileName   : translateNum.py
    Author     : Honghe
    Descreption: 剑指 Offer 46. 把数字翻译成字符串
"""

class Solution(object):
    def translateNum(self, num):
        """
        :type num: int
        :rtype: int
        """
        str_num = str(num)
        num_len = len(str_num)
        dp = [1]*num_len
        res = []
        for i in range(1,num_len):
            if str_num[num_len-i-1]!='0' and int(str_num[num_len-i-1:num_len-i+1])<26:
                if i == 1:
                    dp[i] = dp[i - 1]+1
                else:
                    dp[i] = dp[i - 1] + dp[i - 2]
            else:
                dp[i] = dp[i - 1]
        return dp[-1]

if __name__ == '__main__':
    sol = Solution()
    num = 506
    print(sol.translateNum(num))
