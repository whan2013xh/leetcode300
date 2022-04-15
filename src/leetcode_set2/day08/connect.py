# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-04-15
    FileName   : connect.py
    Author     : Honghe
    Descreption: 
"""
import copy
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution(object):
    def connect(self, root):
        """
        层次遍历
        :type root: Node
        :rtype: Node
        """
        queue = [root]
        tmp = []
        while queue:
            node = queue.pop(0)
            node.next = queue[0] if queue else None
            if node.left:
                tmp.append(node.left)
            if node.right:
                tmp.append(node.right)
            if not queue:
                queue = tmp
                tmp = []
        return root

if __name__ == '__main__':
    sol = Solution()
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)
    node6 = Node(6)
    node7 = Node(7)
    node1.left = node2
    node1.right = node3
    node2.left = node4
    node2.right = node5
    node3.left = node6
    node3.right = node7
    print(sol.connect(node1))

