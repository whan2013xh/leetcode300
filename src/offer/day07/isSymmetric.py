# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-03-29
    FileName   : isSymmetric.py
    Author     : Honghe
    Descreption: 剑指 Offer 28. 对称的二叉树
"""

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        return self.is_same(root.left,root.right)


    def is_same(self,A,B):
        if A is None and B is None:
            return True
        if not(A is not None and B is not None and A.val==B.val):
            return False
        return self.is_same(A.left,B.right)&self.is_same(A.right,B.left)