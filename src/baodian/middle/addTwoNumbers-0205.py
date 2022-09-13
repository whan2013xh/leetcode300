# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-08-26
    FileName   : addTwoNumbers-0205.py
    Author     : Honghe
    Descreption: 
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        直接遍历
        :param l1:
        :param l2:
        :return:
        """
        head1= l1
        head2 = l2
        flag = 0
        while l1 and l2:
            l1 = l1.next
            l2 = l2.next
        res = head1 if l1 else head2
        l1 = head1
        l2 = head2
        new_head = ListNode(0,res)
        pre = new_head
        while res:
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0
            tmp = l1_val+l2_val+flag
            if tmp>=10:
                flag = 1
            else:
                flag = 0
            tmp =tmp%10
            res.val = tmp
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            pre = res
            res = res.next

        if flag==1:
            pre.next = ListNode(1)
        return new_head.next





