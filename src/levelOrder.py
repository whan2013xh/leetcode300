# -*- coding: utf-8 -*-
"""
    CreatedDate: 2021/7/25 19:20
    FileName   : levelOrder.py
    Author     : xuhan
    Descreption: 
"""
import copy

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def levelOrder(self, root):
        """
        bfs:广度优先遍历
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        res = []
        quene = []
        quene.append(root)

        while len(quene)>0:
            size = len(quene)
            level_list = []

            while size>0:
                cur = quene.pop(0)

                if cur.left is not None:
                    quene.append(cur.left)
                if cur.right is not None:
                    quene.append(cur.right)
                size -= 1
                level_list.append(cur.val)
            res.append(copy.deepcopy(level_list))
        return res

    def levelOrder2(self, root):
        """
        dfs:深度优先遍历，使用DFS来进行层次遍历需要知道遍历的节点所在的层
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        self.dfs(root, res, 0)
        return res

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
    res = sol.levelOrder2(root)
    print(res)
