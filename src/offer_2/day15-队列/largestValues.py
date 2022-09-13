# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-06-22
    FileName   : largestValues.py
    Author     : Honghe
    Descreption: 
"""
from typing import List
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        res = []
        if not root:
            return res
        nodes_deque = deque()
        nodes_deque.append(root)
        while nodes_deque:
            level_size = len(nodes_deque)
            level_max = float("-inf")
            for i in range(level_size):
                tmp = nodes_deque.popleft()
                level_max = max(level_max,tmp.val)
                if tmp.left:
                    nodes_deque.append(tmp.left)
                if tmp.right:
                    nodes_deque.append(tmp.right)
            res.append(level_max)

        return res


