# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-06-07
    FileName   : removeNthFromEnd.py
    Author     : Honghe
    Descreption: 剑指 Offer II 021. 删除链表的倒数第 n 个结点
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        new_head = ListNode()
        new_head.next = head
        fast = head
        slow = head
        pre = new_head
        while n>0:
            fast = fast.next
            n-=1

        while fast is not None:
            fast = fast.next
            pre = slow
            slow = slow.next

        pre.next = slow.next
        return new_head.next


