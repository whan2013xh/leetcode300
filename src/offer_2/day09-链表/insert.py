# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-06-15
    FileName   : insert.py
    Author     : Honghe
    Descreption: 剑指 Offer II 029. 排序的循环链表
"""


# Definition for a Node.
class Node(object):
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def insert(self, head, insertVal):
        """
        :type head: Node
        :type insertVal: int
        :rtype: Node
        """
        insert_node = Node(insertVal)
        if not head:
            insert_node.next = insert_node
            return insert_node

        cur = head
        while cur.next!=head:
            next = cur.next

            if next.val>=insertVal>=cur.val or (cur.val>next.val>insertVal) or (insertVal>cur.val>next.val):
                break

            cur = next
        insert_node.next = cur.next
        cur.next = insert_node
        return head
