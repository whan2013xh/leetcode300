# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-08-31
    FileName   : inorderSuccessor-0406.py
    Author     : Honghe
    Descreption: 
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> TreeNode:
        """
        中序遍历即可
        :param root:
        :param p:
        :return:
        """
        self.flag = False
        res = self.in_order(root,p)
        return res

    def in_order(self,root,p):
        if not root:
            return None

        if root==p:
            self.flag = True
            return self.in_order(root.right,p)
        res = None
        if root.val>p.val and root.left:
            res = self.in_order(root.left, p)
        if self.flag:
            return root if res is None else res
        if root.val<p.val and root.right:
            res = self.in_order(root.right, p)
        return res

if __name__ == '__main__':
    node1 = TreeNode(2)
    node2 = TreeNode(1)
    node3 =TreeNode(3)
    node1.left = node2
    node1.right = node3
    sol = Solution()
    p = node2
    print(sol.inorderSuccessor(node1,p))
