# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-06-08
    FileName   : getIntersectionNode.py
    Author     : Honghe
    Descreption: 剑指 Offer II 023. 两个链表的第一个重合节点
"""

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if headA is None or headB is None:
            return None
        pos1 = headA
        pos2 = headB

        while pos1!=pos2:
            pos1 = pos1.next
            pos2 = pos2.next

            if pos1 is None:
                pos1 = headB
            if pos2 is None:
                pos2 = headA
        return pos1