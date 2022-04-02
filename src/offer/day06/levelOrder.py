# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-03-29
    FileName   : levelOrder.py
    Author     : Honghe
    Descreption: 剑指 Offer 32 - I. 从上到下打印二叉树
"""

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        层次遍历
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        stack = []
        stack.append(root)
        res = []
        while stack:
            cur = stack.pop(0)
            res.append(cur.val)
            if cur.left:
                stack.append(cur.left)
            if cur.right:
                stack.append(cur.right)
        return res

