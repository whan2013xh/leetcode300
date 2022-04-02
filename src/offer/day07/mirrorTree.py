# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-03-29
    FileName   : mirrorTree.py
    Author     : Honghe
    Descreption: 剑指 Offer 27. 二叉树的镜像
"""

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def mirrorTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return
        left = root.left
        right = root.right
        root.right=left
        root.left = right
        self.mirrorTree(root.left)
        self.mirrorTree(root.right)
        return root


