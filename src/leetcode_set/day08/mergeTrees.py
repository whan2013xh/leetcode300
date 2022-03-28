# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-03-15
    FileName   : mergeTrees.py
    Author     : Honghe
    Descreption: 617. 合并二叉树
"""

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def mergeTrees(self, root1, root2):
        """
        递归法
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: TreeNode
        """
        if not root1:
            return root2
        if not root2:
            return root1
        root1.val +=root2.val
        root1.left = self.mergeTrees(root1.left, root2.left)
        root1.right = self.mergeTrees(root1.right, root2.right)
        return root1


    def mergeTrees2(self, root1, root2):
        if not root1:
            return root2
        if not root2:
            return root1

        queue = [[root1,root2]]
        while queue:
            r1, r2 = queue.pop(0)
            if r1.left and r2.left:
                r1.left.val = r1.left.val+r2.left.val
            elif not r1.left:
                r1.left.val = r2.left.val
            if r1.right and r2.right:
                r1.right.val = r1.right.val + r2.right.val
            elif not r1.right:
                r1.right.val = r2.right.val
        return root1



