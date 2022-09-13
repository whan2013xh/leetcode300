# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-08-26
    FileName   : detectCycle-0208.py
    Author     : Honghe
    Descreption: 
"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        """
        快慢指针
        :param head:
        :return:
        """
        fast = head
        slow = head
        while slow and fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                break
        if fast.next:
            fast = head
            while fast!=slow:
                fast=fast.next
                slow = slow.next
            return fast

        return None