# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-03-17
    FileName   : reverseList.py
    Author     : Honghe
    Descreption: 剑指 Offer 24. 反转链表
"""

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        pre = None
        cur = head
        while cur:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
        return pre