# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-08-30
    FileName   : listOfDepth-0403.py
    Author     : Honghe
    Descreption: 
"""
from typing import List
from queue import Queue


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def listOfDepth(self, tree: TreeNode) -> List[ListNode]:
        if not tree:
            return []

        nodes = []
        nodes.append(tree)
        level_nodes = []
        while nodes:
            new_head = None
            pre_node = None
            level = len(nodes)
            for i in range(level):
                cur_node = nodes.pop()
                if cur_node.left:
                    nodes.append(cur_node.left)
                if cur_node.right:
                    nodes.append(cur_node.right)
                node = ListNode(cur_node.val)
                if new_head is None:
                    new_head = node
                else:
                    pre_node.next = node
                pre_node = node
            level_nodes.append(new_head)
        return level_nodes


