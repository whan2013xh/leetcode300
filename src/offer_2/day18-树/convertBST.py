# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-06-23
    FileName   : convertBST.py
    Author     : Honghe
    Descreption: 
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        node_list = []
        self.dfs(root,node_list,0)
        return root


    def dfs(self, node, node_list,pre):
        if not node:
            return 0

        if not node.left and not node.right:
            node.val += pre
            return node.val

        if node.right:
            node.val += self.dfs(node.right,node_list,pre)
        else:
            node.val += pre

        if node.left:
            pre = node.val
            return self.dfs(node.left,node_list,pre)

        return node.val

if __name__ == '__main__':
    [3, 2, 4, 1]
    node1 = TreeNode(3)
    node2 = TreeNode(2)
    node3 = TreeNode(4)
    node4 = TreeNode(1)
    node5 = TreeNode(2)
    node6 = TreeNode(5)
    node7 = TreeNode(7)
    node8 = TreeNode(3)
    node9 = TreeNode(8)
    node1.left =node2
    node1.right = node3
    node2.left = node4
    # node2.right = node5
    # node3.left = node6
    # node3.right = node7
    # node5.right = node8
    # node7.right = node9
    sol = Solution()
    print(sol.convertBST(node1))



