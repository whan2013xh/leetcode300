# -*- coding: utf-8 -*-
"""
    CreatedDate: 2021/7/26 20:07
    FileName   : levelOrderBottom.py
    Author     : xuhan
    Descreption: 107. 二叉树的层序遍历 II
"""
import copy


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def levelOrderBottom(self, root):
        """
        bfs:和102到题目一样，只是返回结果时倒序就行
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []

        res = []
        queue = []
        queue.append(root)
        while len(queue) > 0:
            size = len(queue)
            level_list = []
            while size > 0:
                cur = queue.pop(0)
                if cur.left is not None:
                    queue.append(cur.left)
                if cur.right is not None:
                    queue.append(cur.right)
                size -= 1
                level_list.append(cur.val)
            res.append(copy.deepcopy(level_list))
        return res[::-1]

    def levelOrderBottom2(self, root):
        """
        dfs:和102到题目一样，只是返回结果时倒序就行
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        res = []
        self.dfs(root, res, 0)
        return res[::-1]

    def dfs(self, node, res, level):
        if node is None:
            return
        if len(res)<level+1:
            res.append([])
        if node.left is not None:
            self.dfs(node.left, res, level+1)
        if node.right is not None:
            self.dfs(node.right, res, level+1)
        res[level].append(node.val)

if __name__ == '__main__':
    # [3, 9, 20, null, null, 15, 7],
    root = TreeNode(3)
    left_node1 = TreeNode(9)
    right_node1 = TreeNode(20)
    left_node2 = TreeNode(15)
    right_node2 = TreeNode(7)
    root.left = left_node1
    root.right = right_node1
    right_node1.left = left_node2
    right_node1.right = right_node2
    sol =Solution()
    res = sol.levelOrderBottom2(root)
    print(res)