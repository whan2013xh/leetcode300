# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-06-14
    FileName   : flatten.py
    Author     : Honghe
    Descreption: 剑指 Offer II 028. 展平多级双向链表
"""

# Definition for a Node.
class Node(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


class Solution(object):
    def flatten(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        self.dfs(head)
        return head


    def dfs(self, head):
        cur = head
        last = None
        while cur is not None:
            next = cur.next
            if cur.child:
                last_child = self.dfs(cur.child)
                cur.next = cur.child
                cur.child.prev = cur
                if next:
                    last_child.next = next
                    next.prev = last_child

                cur.child = None
                last = last_child
            else:
                last = cur
            cur = next
        return last


if __name__ == '__main__':
    node1 = Node(1,None,None,None)
    node2 = Node(2, None, None, None)
    node3 = Node(3, None, None, None)
    node4 = Node(4, None, None, None)
    node5 = Node(5, None, None, None)
    node6 = Node(6, None, None, None)
    node7 = Node(7, None, None, None)
    node8 = Node(8, None, None, None)
    node9 = Node(9, None, None, None)
    node11 = Node(11, None, None, None)
    node12 = Node(12, None, None, None)

    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node6

    node2.prev = node1
    node3.prev = node2
    node4.prev = node3
    node5.prev = node4
    node6.prev = node5

    node3.child = node7

    node7.next= node8
    node8.prev = node7

    node8.child = node11
    node11.next=node12
    node12.prev=node11
    # node8.next = node9
    # node9.prev=node8
    # node8.prev = node7

    # node1.child=node2
    # node2.child=node3

    sol = Solution()
    print(sol.flatten(node1))
