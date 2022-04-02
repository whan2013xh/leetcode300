# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-04-01
    FileName   : deleteNode.py
    Author     : Honghe
    Descreption: 剑指 Offer 18. 删除链表的节点
"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        new_head = ListNode(0)
        new_head.next = head
        pre = new_head
        cur = head
        while cur:
           if cur.val==val:
               pre.next = cur.next
               break
           pre = cur
           cur = cur.next
        return new_head.next


