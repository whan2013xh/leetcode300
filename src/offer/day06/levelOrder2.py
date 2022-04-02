# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-03-29
    FileName   : levelOrder.py
    Author     : Honghe
    Descreption: 剑指 Offer 32 - II. 从上到下打印二叉树 II
"""
import copy

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        层次遍历
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        stack = []
        stack.append(root)
        res = [[root.val]]
        tmp_level = []
        while stack:
            cur = stack.pop(0)
            # tmp_level.append(cur.val)
            if cur.left:
                tmp_level.append(cur.left)
            if cur.right:
                tmp_level.append(cur.right)
            if not stack and tmp_level:
               res.append([node.val for node in tmp_level])
               stack = copy.deepcopy(tmp_level)
               tmp_level = []
        return res

if __name__ == '__main__':
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(4)
    node5 = TreeNode(5)
    node1.left = node2
    node1.right = node3
    node2.left = node4
    node2.right = node5
    sol = Solution()
    print(sol.levelOrder(node1))

