# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-08-30
    FileName   : isValidBST-0405.py
    Author     : Honghe
    Descreption: 
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        return self.is_bst(root,float("-inf"),float("inf"))

    def is_bst(self,root,left_val,right_val):
        if root is None:
            return True

        if root.left and (root.left.val>=root.val or root.left.val<=left_val):
            return False
        if root.right and (root.right.val<=root.val or root.right.val>=right_val):
            return False
        return self.is_bst(root.left,left_val,root.val) and self.is_bst(root.right,root.val,right_val)

if __name__ == '__main__':
    # [10, 5, 15, null, null, 6, 20]
    pass
