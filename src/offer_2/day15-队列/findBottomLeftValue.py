# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-06-22
    FileName   : findBottomLeftValue.py
    Author     : Honghe
    Descreption: 剑指 Offer II 045. 二叉树最底层最左边的值
"""
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        nodes = deque()
        nodes.append(root)

        while nodes:
            level_size = len(nodes)
            level_nodes = []
            for _ in range(level_size):
                node = nodes.popleft()
                level_nodes.append(node)
                if node.left:
                    nodes.append(node.left)
                if node.right:
                    nodes.append(node.right)
        return level_nodes[0].val





