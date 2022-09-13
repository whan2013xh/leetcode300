# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-07-29
    FileName   : BSTSequences-0409.py
    Author     : Honghe
    Descreption: 面试题 04.09. 二叉搜索树序列
"""
from typing import List

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def BSTSequences(self, root: TreeNode) -> List[List[int]]:
        """
        递归+排列组合：自底向上
        :param root:
        :return:
        """
        if not root:
            return [[]]
        if root.left is None and root.right is None:
            return [[root.val]]
        left_tree = root.left
        right_tree = root.right
        return self.combine(self.BSTSequences(left_tree), self.BSTSequences(right_tree), root.val)

    def combine(self,left_trees,right_trees,root):
        """
        合并
        :param left_trees: 左子树所有的排列组合
        :param right_trees: 右子树所有的排列组合
        :param root:
        :return:
        """
        res = []
        if not left_trees[0] or not right_trees[0]:
            return [[root]+i for i in left_trees] if left_trees[0] else [[root]+i for i in right_trees]
        for i in left_trees:
            for j in right_trees:
                path = [root]
                self.perm(i,j,path,res)
        return res

    def perm(self,left,right,path,res):
        """
        左右子树合并，保证左右子树各自的顺序不变即可
        :param left:
        :param right:
        :param path:
        :param res:
        :return:
        """
        if not left and not right:
            res.append(path[:])
            return
        if left:
            path.append(left[0])
            next_left = [] if len(left)==1 else left[1:]
            self.perm(next_left,right,path,res)
            path.pop()
        if right:
            path.append(right[0])
            next_right = [] if len(right) == 1 else right[1:]
            self.perm(left, next_right, path,res)
            path.pop()

    def BSTSequences2(self, root: TreeNode) -> List[List[int]]:
        """
        层次遍历+回溯法
        :param root:
        :return:
        """
        if not root:
            return [[]]
        queue = [root]
        res = []
        path = []
        self.find_path(queue,res,path)
        return res

    def find_path(self,queue,res,path):
        length = len(queue)
        for i in range(length):
            node = queue[i]
            new_queue = queue[:i]+queue[i+1:]
            path.append(node.val)
            if node.left:
                new_queue.append(node.left)
            if node.right:
                new_queue.append(node.right)
            if not new_queue:
                res.append(path[:])
                path.pop()
                return
            self.find_path(new_queue,res,path)
            path.pop()

if __name__ == '__main__':
    sol = Solution()
    node1 = TreeNode(5)
    node2 = TreeNode(2)
    node3 = TreeNode(1)
    node4 = TreeNode(4)
    node5 = TreeNode(3)
    node1.left = node2
    node2.left = node3
    node2.right = node4
    node4.left=node5
    print(sol.BSTSequences2(node1))
    # a = ["a","b"]
    # b = ["1","2"]
    # res = []
    # path = []
    # sol.perm(a,b,path,res)
    # print(res)