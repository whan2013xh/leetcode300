# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-06-08
    FileName   : reverseList.py
    Author     : Honghe
    Descreption: 剑指 Offer II 024. 反转链表
"""

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        cur = head
        pre = None
        while cur is not None:
            next = cur.next
            cur.next = pre
            pre = cur
            cur = next
        return pre
