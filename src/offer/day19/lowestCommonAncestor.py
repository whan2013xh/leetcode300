# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-04-11
    FileName   : lowestCommonAncestor.py
    Author     : Honghe
    Descreption: 剑指 Offer 68 - I. 二叉搜索树的最近公共祖先
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
        min_node = min(p.val,q.val)
        max_node = max(p.val,q.val)
        return self.find(root,min_node, max_node)

    def find(self,root,min_node,max_node):
        if not root:
            return None
        if root.val>max_node:
            return self.find(root.left, min_node, max_node)
        if root.val<min_node:
            return self.find(root.right, min_node, max_node)
        return root
