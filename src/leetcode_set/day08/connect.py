# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-03-15
    FileName   : connect.py
    Author     : Honghe
    Descreption: 
"""
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        level_nodes = [root]
        tmp_level = []
        while level_nodes:
            cur = level_nodes.pop(0)
            if cur and cur.left:
                tmp_level.append(cur.left)
            if cur and cur.right:
                tmp_level.append(cur.right)
            if not level_nodes:

                level_nodes = tmp_level
                tmp_level = []
            else:
                cur.next = level_nodes[0]
        return root
