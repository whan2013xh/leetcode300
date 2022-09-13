# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-06-14
    FileName   : isPalindrome.py
    Author     : Honghe
    Descreption: 
"""

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        values = []
        while head:
            values.append(head.val)
            head = head.next

        return values==values[::-1]
