# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-06-08
    FileName   : addTwoNumbers.py
    Author     : Honghe
    Descreption: 剑指 Offer II 025. 链表中的两数相加
"""

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        num1 = []
        while l1 is not None:
            num1.append(str(l1.val))
            l1 = l1.next

        num2 = []
        while l2 is not None:
            num2.append(str(l2.val))
            l2 = l2.next

        res = str(int("".join(num1))+int("".join(num2)))
        head = ListNode(int(res[0]))
        cur =head
        for i in res[1:]:
            tmp = ListNode(int(i))
            cur.next = tmp
            cur = tmp
        return head

if __name__ == '__main__':
    a = [1,2,3]
    "".join(a)
