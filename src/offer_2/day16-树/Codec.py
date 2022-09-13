# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-06-22
    FileName   : Codec.py
    Author     : Honghe
    Descreption: 剑指 Offer II 048. 序列化与反序列化二叉树
"""
from collections import deque

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        bfsC层次遍历
        :type root: TreeNode
        :rtype: str
        """
        res = []
        if not root:
            return ""
        nodes = deque()
        nodes.append(root)

        while nodes:
            node = nodes.popleft()
            if node:
                res.append(str(node.val))
                nodes.append(node.left)
                nodes.append(node.right)
            else:
                res.append("None")
        return ",".join(res)


    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None

        data_nodes = data.split(",")
        root_val = data_nodes[0]
        root = TreeNode(root_val)
        tree_nodes = deque([root])
        i = 1
        while tree_nodes:
            node = tree_nodes.popleft()
            if data_nodes[i]!="None":
                left_node = TreeNode(int(data_nodes[i]))
                node.left = left_node
                tree_nodes.append(left_node)

            i+=1

            if data_nodes[i] != "None":
                right_node = TreeNode(int(data_nodes[i]))
                node.right = right_node
                tree_nodes.append(right_node)
            i+=1
        return root







