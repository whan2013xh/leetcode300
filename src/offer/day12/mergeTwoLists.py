# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-04-01
    FileName   : mergeTwoLists.py
    Author     : Honghe
    Descreption: 剑指 Offer 25. 合并两个排序的链表
"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2
        if not l2:
            return l1
        res = ListNode(0)
        pos = res
        while l1 and l2:
            if l1.val>=l2.val:
                pos.next = l2
                l2 = l2.next
            else:
                pos.next = l1
                l1 = l1.next
            pos = pos.next
        if l1:
            pos.next = l1
        elif l2:
            pos.next = l2
        return res.next