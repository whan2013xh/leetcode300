# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-06-22
    FileName   : rightSideView.py
    Author     : Honghe
    Descreption: 剑指 Offer II 046. 二叉树的右侧视图

"""
from typing import List
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        res = []
        if not root:
            return res
        nodes = deque()
        nodes.append(root)

        while nodes:
            level_size = len(nodes)
            res.append(nodes[-1].val)
            for _ in range(level_size):
                node = nodes.popleft()
                if node.left:
                    nodes.append(node.left)
                if node.right:
                    nodes.append(node.right)
        return res


