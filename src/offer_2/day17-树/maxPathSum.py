# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-06-23
    FileName   : maxPathSum.py
    Author     : Honghe
    Descreption: 剑指 Offer II 051. 节点之和最大的路径
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    max_res = float("-inf")
    def maxPathSum(self, root: TreeNode) -> int:
        self.dfs(root)
        return self.max_res


    def dfs(self, node):
        if not node:
            return float("-inf")
        res = node.val
        left_tree = self.dfs(node.left)
        right_tree = self.dfs(node.right)
        self.max_res = max(self.max_res, res, res+left_tree,res+right_tree, res+left_tree+right_tree,left_tree,right_tree)
        return max(res,res+left_tree,res+right_tree)
