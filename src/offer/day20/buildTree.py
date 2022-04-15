# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-04-11
    FileName   : buildTree.py
    Author     : Honghe
    Descreption: 剑指 Offer 07. 重建二叉树
"""
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not preorder:
            return
        root=TreeNode(preorder[0])
        center_index = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:center_index+1],inorder[:center_index])
        root.right = self.buildTree(preorder[center_index+1:],inorder[center_index+1:])
        return root

if __name__ == '__main__':
    sol = Solution()
    preorder = [1,2,3]
    inorder = [3,2,1]
    print(sol.buildTree(preorder,inorder))