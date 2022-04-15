# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-04-06
    FileName   : pathSum.py
    Author     : Honghe
    Descreption: 剑指 Offer 34. 二叉树中和为某一值的路径
"""
import copy
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def pathSum(self, root, target):
        """
        回溯
        :type root: TreeNode
        :type target: int
        :rtype: List[List[int]]
        """
        # badcase
        if not root:
            return []
        path = [root.val]
        path_list = []

        self.find_path(root,target,path,path_list)
        return path_list

    def find_path(self,root,target,path,path_list):
        if not root:
            return False
        if root.val == target and not root.left and not root.right:
            path_list.append(copy.deepcopy(path))
            return True
        if root.left:
            path.append(root.left.val)
            self.find_path(root.left,target-root.val,path,path_list)
            path.pop()
        if root.right:
            path.append(root.right.val)
            self.find_path(root.right, target - root.val, path, path_list)
            path.pop()
        return


if __name__ == '__main__':
    sol = Solution()
    node1 = TreeNode(1)
    node2 = TreeNode(-2)
    node3 = TreeNode(-3)
    node1.right = node2
    print(sol.pathSum(node1,-5))

