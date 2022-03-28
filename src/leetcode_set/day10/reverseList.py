# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-03-17
    FileName   : reverseList.py
    Author     : Honghe
    Descreption: 206. 反转链表
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
        pre = None
        cur = head
        while cur:
            next = cur.next
            cur.next = pre
            pre = cur
            cur = next
        return pre