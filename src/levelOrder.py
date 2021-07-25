# -*- coding: utf-8 -*-
"""
    CreatedDate: 2021-07-25
    FileName   : levelOrder.py
    Author     : Honghe
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
        BFS：广度优先遍历，使用队列这种结构来辅助
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
            level_res = []
            while size>0:
                cur = quene.pop(0)
                if cur.left is not None:
                    quene.append(cur.left)
                if cur.right is not None:
                    quene.append(cur.right)
                size -= 1
                level_res.append(cur.val)
            res.append(copy.deepcopy(level_res))

        return res

    def levelOrder2(self, root):
        """
        DFS：深度优先遍历，其实使用DFS来进行层次遍历，就是得知道每次遍历的节点它所在的层次才能把结果输出
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        self.bfs()

    def bfs(self, node, res, level):
        if node is None:
            return
        if len(res)<level+1:
            res.append([])

        if node.left is not None:
            self.bfs(node.left, res, level+1)
        if node.right is not None:
            self.bfs(node.right, )



if __name__ == '__main__':
    nodes = [3, 9, 20, None, None, 15, 7]
    root = TreeNode(3)
    left_node1 = TreeNode(9, None, None)
    right_node1 = TreeNode(20)
    root.left = left_node1
    root.right = right_node1
    left_node2 = TreeNode(15, None, None)
    right_node2 = TreeNode(7, None, None)
    right_node1.left = left_node2
    right_node1.right = right_node2
    sol = Solution()
    res = sol.levelOrder(root)
    print(res)



