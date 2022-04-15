# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-04-15
    FileName   : isSubtree.py
    Author     : Honghe
    Descreption: 572. 另一棵树的子树
"""

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def isSubtree(self, root, subRoot):
        """
        :type root: TreeNode
        :type subRoot: TreeNode
        :rtype: bool
        """
        queue = [root]
        while queue:
            node = queue.pop()
            if node.val == subRoot.val:
                res = self.dfs(node, subRoot)
                if res:
                    return True
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return False



    def dfs(self, root, subRoot):
        queue = [root]
        queue2 = [subRoot]
        while queue and queue2:
            node1 = queue.pop()
            node2 = queue2.pop()
            if node1.val!=node2.val:
                return False
            if node2.left:
                if not node1.left or node1.left.val!=node2.left.val:
                    return False
                queue.append(node1.left)
                queue2.append(node2.left)
            elif node1.left:
                return False
            if node2.right:
                if not node1.right or node1.right.val!=node2.right.val:
                    return False
                queue.append(node1.right)
                queue2.append(node2.right)
            elif node1.right:
                return False
        return True

    def isSubtree2(self, root, subRoot):
        if not root and not subRoot:
            return True
        if not root or not subRoot:
            return False
        return self.isSameTree(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def isSameTree(self, s, t):
        if not s and not t:
            return True
        if not s or not t:
            return False
        return s.val == t.val and self.isSameTree(s.left, t.left) and self.isSameTree(s.right, t.right)




