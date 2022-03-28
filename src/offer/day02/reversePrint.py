# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-03-17
    FileName   : reversePrint.py
    Author     : Honghe
    Descreption: 
"""
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reversePrint(self, head):
        """
        :type head: ListNode
        :rtype: List[int]
        """
        res = []
        while head:
            res.append(head.val)
            head = head.next
        return res[::-1]