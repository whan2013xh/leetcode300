# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-04-11
    FileName   : lowestCommonAncestor2.py
    Author     : Honghe
    Descreption: 剑指 Offer 68 - II. 二叉树的最近公共祖先
"""
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        return self.find(root,p,q)

    def find(self,root,p,q):
        if not root:
            return None
        # 要理解这行代码的意思
        if root.val==p.val or root.val==q.val:
            return root
        left = self.find(root.left,p,q)
        right = self.find(root.right,p,q)
        if left is not None and right is not None:
            return root
        return left if left is not None else right