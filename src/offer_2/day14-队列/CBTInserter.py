# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-06-22
    FileName   : CBTInserter.py
    Author     : Honghe
    Descreption: 剑指 Offer II 043. 往完全二叉树添加节点
"""
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class CBTInserter:

    def __init__(self, root: TreeNode):
        self.root = root
        self.nodes = deque()

        trace_nodes=deque()
        trace_nodes.append(root)
        while trace_nodes:
            level_nodes = len(trace_nodes)
            for i in range(level_nodes):
                tmp_node = trace_nodes.popleft()
                if tmp_node.left:
                    trace_nodes.append(tmp_node.left)
                else:
                    self.nodes.append(tmp_node)
                    continue
                if tmp_node.right:
                    trace_nodes.append(tmp_node.right)
                else:
                    self.nodes.append(tmp_node)


    def insert(self, v: int) -> int:
        node = TreeNode(v)
        father_node = self.nodes[0]
        if not father_node.left:
            father_node.left = node
        else:
            father_node.right = node
            self.nodes.popleft()
        self.nodes.append(node)
        return father_node.val



    def get_root(self) -> TreeNode:
        return self.root

if __name__ == '__main__':
    root = TreeNode(1)
    sol = CBTInserter(root)
    print(sol.insert(2))
    print(sol.insert(3))
    print(sol.insert(4))