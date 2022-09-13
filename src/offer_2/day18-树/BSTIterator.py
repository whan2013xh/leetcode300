# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-06-24
    FileName   : BSTIterator.py
    Author     : Honghe
    Descreption: 剑指 Offer II 055. 二叉搜索树迭代器
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class BSTIterator:

    def __init__(self, root: TreeNode):
        self.node_list = []
        self.dfs(root,self.node_list)
        self.index = 0


    def next(self) -> int:
        node = self.node_list[self.index]
        self.index+=1
        return node.val

    def hasNext(self) -> bool:
        return self.index<len(self.node_list)

    def dfs(self,node,node_list):
        if not node:
            return
        if node.left:
            self.dfs(node.left,node_list)

        node_list.append(node)

        if node.right:
            self.dfs(node.right,node_list)
