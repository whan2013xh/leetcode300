# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-03-17
    FileName   : mergeTwoLists.py
    Author     : Honghe
    Descreption: 21. 合并两个有序链表
"""

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: O
        """
        new_head = ListNode(0)
        head = new_head
        while list1 and list2:
            if list1.val <= list2.val:
                head.next = list1
                list1 = list1.next
            else:
                head.next = list2
                list2 = list2.next
            head = head.next
        if list1:
            head.next = list1
        elif list2:
            head.next = list2
        return new_head.next


