# -*- coding: utf-8 -*-
"""
    CreatedDate: 2021-07-29
    FileName   : reverseList.py
    Author     : Honghe
    Descreption: 206. 反转链表
"""

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def reverseList(self, head):
        """
        迭代法：
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return head
        cur = head
        prev = None
        while cur is not None:
           tmp = cur.next
           cur.next = prev
           prev = cur
           cur = tmp
        return prev

    def reverseList2(self, head):
        """
        递归法
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        p = self.reverseList2(head.next)
        # 下面这行代码是关键，它实现的就是链表反转
        head.next.next = head
        head.next = None
        return p

if __name__ == '__main__':
    head = [1, 2, 3, 4, 5]
    prev = None
    first = None
    for i in head:
        node = ListNode(i, None)
        if prev is not None:
            prev.next = node
        if prev is None:
            first = node
        prev = node

    sol = Solution()
    res = sol.reverseList2(first)
    print()


