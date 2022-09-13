# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-06-23
    FileName   : sumNumbers.py
    Author     : Honghe
    Descreption: 
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        pre_list = []
        paths = []
        self.dfs(root,pre_list,paths)
        return sum(paths)

    def dfs(self, node, pre_list, paths):
        if not node:
            return
        if not node.left and not node.right:
            path = int("".join(pre_list)+str(node.val))
            paths.append(path)
            return
        else:
            pre_list.append(str(node.val))
            self.dfs(node.left,pre_list,paths)
            self.dfs(node.right,pre_list,paths)
            pre_list.pop()

