# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-06-24
    FileName   : findTarget.py
    Author     : Honghe
    Descreption: 剑指 Offer II 056. 二叉搜索树中两个节点之和

"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        node_list = {}
        res = self.dfs(root,node_list,k)
        return res


    def dfs(self, node, node_list,target):
        if not node:
            return False
        res = False
        if node.left:
            res = self.dfs(node.left,node_list,target)
            if res:
                return True
        if target-node.val in node_list:
            return True

        node_list[node.val] = 1

        if node.right:
            res = self.dfs(node.right,node_list)
        return res
