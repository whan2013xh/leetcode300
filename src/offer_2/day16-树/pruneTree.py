# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-06-22
    FileName   : pruneTree.py
    Author     : Honghe
    Descreption: 剑指 Offer II 047. 二叉树剪枝

"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:
        self.cut_tree(root)
        return root


    def cut_tree(self, root):
        if not root:
            return None

        left_zero = self.cut_tree(root.left)
        right_zero = self.cut_tree(root.right)

        if left_zero is None:
            root.left = None
        if right_zero is None:
            root.right = None

        if root.val==0 and left_zero is None and right_zero is None:
            root = None
            return None
        return root




