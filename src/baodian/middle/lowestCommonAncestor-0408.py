# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-08-31
    FileName   : lowestCommonAncestor-0408.py
    Author     : Honghe
    Descreption: 
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root:
            return None
        # 如果根节点就是想要查找的元素
        if p==root or q==root:
            return root
        left_res = self.lowestCommonAncestor(root.left,p,q)
        right_res = self.lowestCommonAncestor(root.right,p,q)
        # 如果两个节点分别在左右子树中
        if left_res and right_res:
            return root
        # 如果在同一个子树中，先找到的节点就是相同祖先节点
        return left_res if left_res else right_res



if __name__ == '__main__':
    sol = Solution()
    root = [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]
    nodes = []
    for i in root:
        if i is None:
            nodes.append(i)
        else:
            nodes.append(TreeNode(i))
    for i,node in enumerate(nodes):
        if 2*i+1<len(nodes):
            node.left = nodes[2*i+1]
        if 2*i+2<len(nodes):
            node.right = nodes[2 * i + 2]
    p = nodes[1]
    q = nodes[-1]
    res = sol.lowestCommonAncestor(nodes[0],p,q)
    print(res.val)





