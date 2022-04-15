# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-04-11
    FileName   : verifyPostorder.py
    Author     : Honghe
    Descreption: 剑指 Offer 33. 二叉搜索树的后序遍历序列
"""

class Solution(object):
    def verifyPostorder(self, postorder):
        """
        :type postorder: List[int]
        :rtype: bool
        """
        # if not postorder:
        #     return False
        if len(postorder)<=1:
            return True
        root = postorder[-1]
        right = len(postorder)-1
        flag = False
        for i in range(len(postorder)-2,-1,-1):
            if postorder[i]>root:
                if flag:
                    return False
                right = i
                continue
            elif postorder[i]<root:
                flag = True
            else:
                return False
        return self.verifyPostorder(postorder[:right]) & self.verifyPostorder(postorder[right:-1])

    def verifyPostorder2(self, postorder: [int]) -> bool:
        def recur(i, j):
            if i >= j: return True
            p = i
            while postorder[p] < postorder[j]: p += 1
            m = p
            while postorder[p] > postorder[j]: p += 1
            return p == j and recur(i, m - 1) and recur(m, j - 1)

        return recur(0, len(postorder) - 1)



if __name__ == '__main__':
    sol = Solution()
    postorder =  [5, 2, -17, -11, 25, 76, 62, 98, 92, 61]
    print(sol.verifyPostorder(postorder))

