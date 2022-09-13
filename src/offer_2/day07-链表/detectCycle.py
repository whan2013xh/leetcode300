# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-06-08
    FileName   : detectCycle.py
    Author     : Honghe
    Descreption: 剑指 Offer II 022. 链表中环的入口节点
"""


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        1、先判断是否有环
        2、判断入环节点
        :type head: ListNode
        :rtype: ListNode
        """
        slow = head
        fast = head
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next
            if fast==slow:
                break

        if fast is None or fast.next is None:
            return None

        slow = head
        while slow!=fast:
            slow = slow.next
            fast = fast.next
        return slow

if __name__ == '__main__':
    sol = Solution()
    head = ListNode(1)
    node1 = ListNode(2)
    node2 = ListNode(3)
    node3 = ListNode(4)
    head.next = node1
    node1.next = node2
    node2.next = node3
    node3.next = node1
    print(sol.detectCycle(head))

