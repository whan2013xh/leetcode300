# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-03-29
    FileName   : isSubStructure.py
    Author     : Honghe
    Descreption: 剑指 Offer 26. 树的子结构
"""


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isSubStructure(self, A, B):
        """
        :type A: TreeNode
        :type B: TreeNode
        :rtype: bool
        """
        if A is None or B is None:
            return False
        if A.val==B.val:
            tmp = self.is_same(A,B)
            if tmp:
                return True
        return self.isSubStructure(A.left,B) | self.isSubStructure(A.right,B)


    def is_same(self,A,B):
        if B is not None and (A is None or (A is not None and A.val!=B.val)):
            return False
        elif B is None:
            return True
        return True&self.is_same(A.left,B.left)&self.is_same(A.right,B.right)


if __name__ == '__main__':
    node1=TreeNode(10)
    node2=TreeNode(12)
    node3=TreeNode(6)
    node4=TreeNode(8)
    node5=TreeNode(3)
    node6=TreeNode(11)
    node11 = TreeNode(10)
    node21 = TreeNode(12)
    node31 = TreeNode(6)
    node41= TreeNode(8)
    node1.left=node2
    node1.right=node3
    node2.left=node4
    node2.right=node5

