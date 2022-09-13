# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-06-23
    FileName   : inorderSuccessor.py
    Author     : Honghe
    Descreption: 
"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    flag = -1
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        node_list = []
        self.in_order(root, p, node_list)
        return None if self.flag==-1 or self.flag==len(node_list) else node_list[self.flag]

    def in_order(self, node, target,node_list):
        if not node:
            return

        if node.left:
            self.in_order(node.left, target,node_list)
        node_list.append(node)
        if node.val == target.val:
            self.flag = len(node_list)
        if node.right:
            self.in_order(node.right, target,node_list)

if __name__ == '__main__':
    node1 = TreeNode(2)
    node2 = TreeNode(1)
    node3 = TreeNode(3)
    node1.left = node2
    node1.right = node3
    sol = Solution()
    print(sol.inorderSuccessor(node1,node2))

