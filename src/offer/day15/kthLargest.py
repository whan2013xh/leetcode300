# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-04-06
    FileName   : kthLargest.py
    Author     : Honghe
    Descreption: 剑指 Offer 54. 二叉搜索树的第k大节点
"""
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def kthLargest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            node_list.append(node.val)
            dfs(node.right)

        node_list = []
        dfs(root)
        return node_list[-k]

