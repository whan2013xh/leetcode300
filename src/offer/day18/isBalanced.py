# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-04-08
    FileName   : isBalanced.py
    Author     : Honghe
    Descreption: 剑指 Offer 55 - II. 平衡二叉树
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        return False if self.dfs(root) is None else True


    def dfs(self, node):
        if not node:
            return 0
        left_depth = self.dfs(node.left)
        if left_depth is None:
            return None
        right_depth = self.dfs(node.right)
        if right_depth is None:
            return None
        if abs(left_depth-right_depth)>1:
            return None
        return max(left_depth,right_depth)+1
