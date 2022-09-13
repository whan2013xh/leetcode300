# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-06-23
    FileName   : pathSum.py
    Author     : Honghe
    Descreption: 剑指 Offer II 050. 向下的路径节点之和
"""



class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:

    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        if not root:
            return 0
        res = self.dfs(root,targetSum)
        res += self.pathSum(root.left,targetSum)
        res += self.pathSum(root.right,targetSum)
        return res


    def dfs(self, node, target):
        if not node:
            return 0
        ret = 0
        if node.val==target:
            ret+=1
        ret += self.dfs(node.left,target-node.val)
        ret += self.dfs(node.right,target-node.val)
        return ret

    def pathSum2(self, root: TreeNode, targetSum: int) -> int:
        nodes = {}
        nodes[0] = 1
        cur = 0
        return self.dfs2(root,targetSum,cur,nodes)


    def dfs2(self, node, target, cur, nodes):
        if not node:
            return 0
        cur += node.val
        res = 0
        res += nodes.get(cur-target,0)
        nodes[cur] = nodes.get(cur,0)+1
        res += self.dfs2(node.left, target, cur, nodes)
        res += self.dfs2(node.right, target, cur, nodes)
        nodes[cur] -=1
        return res



if __name__ == '__main__':
    node1 = TreeNode(0)
    node2 = TreeNode(1)
    node3 = TreeNode(1)
    node4 = TreeNode(4)
    node5 = TreeNode(5)
    node1.left = node2
    node1.right = node3
    # node3.right = node4
    # node4.right = node5

    sol = Solution()
    target = 1
    print(sol.pathSum(node1,target))
