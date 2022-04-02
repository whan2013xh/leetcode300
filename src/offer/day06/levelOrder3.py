# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-03-29
    FileName   : levelOrder3.py
    Author     : Honghe
    Descreption: 剑指 Offer 32 - III. 从上到下打印二叉树 III
"""
import copy


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        stack = []
        stack.append(root)
        res = [[root.val]]
        tmp_level = []
        level = 1
        while stack:
            cur = stack.pop(0)
            # tmp_level.append(cur.val)
            if cur.left:
                tmp_level.append(cur.left)
            if cur.right:
                tmp_level.append(cur.right)
            if not stack and tmp_level:
                tmp = [node.val for node in tmp_level]
                res.append(tmp if level%2==0 else tmp[::-1])
                stack = copy.deepcopy(tmp_level)
                tmp_level = []
                level+=1
        return res
