# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-06-23
    FileName   : increasingBST.py
    Author     : Honghe
    Descreption: 剑指 Offer II 052. 展平二叉搜索树
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        node_list = []
        self.middle_order(root,node_list)
        pre = None
        for i in node_list[::-1]:
            i.left = None
            i.right = pre
            pre = i
        return node_list[0]

    def middle_order(self, node, node_list):
        if not node:
            return
        if node.left:
            self.middle_order(node.left,node_list)
        node_list.append(node)
        if node.right:
            self.middle_order(node.right,node_list)

