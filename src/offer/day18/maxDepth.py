# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-04-08
    FileName   : maxDepth.py
    Author     : Honghe
    Descreption: 剑指 Offer 55 - I. 二叉树的深度
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        res = self.dfs(root)
        return res


    def dfs(self, node):
        if not node:
            return 0
        return max(self.dfs(node.left),self.dfs(node.right))+1