# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-04-01
    FileName   : getKthFromEnd.py
    Author     : Honghe
    Descreption: 剑指 Offer 22. 链表中倒数第k个节点
"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        fast = head
        slow = head
        count = 0
        while fast:
            if count< k:
                count+=1
            else:
                slow = slow.next
            fast = fast.next
        return slow
