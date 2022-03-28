# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-03-14
    FileName   : removeNthFromEnd.py
    Author     : Honghe
    Descreption: 19. 删除链表的倒数第 N 个结点
"""
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        slow = head
        fast = head
        pre = head
        step=0
        while step<n:
            if fast is None:
                return None
            fast = fast.next
            step+=1
        # 边界条件
        if fast is None and n==1:
            return None
        elif fast is None and n!=1:
            head = head.next
            return head


        while fast is not None:
            fast = fast.next
            pre = slow
            slow=slow.next
        pre.next = slow.next
        return head

    def removeNthFromEnd2(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        # 新建一个节点指向原首节点，这一步很关键
        new_head = ListNode(0, head)
        slow=new_head
        fast = head
        for i in range(n):
            fast=fast.next

        while fast is not None:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return new_head.next

if __name__ == '__main__':
    node1=ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)
    node1.next=node2
    node2.next=node3
    node3.next=node4
    node4.next=node5
    sol = Solution()
    res = sol.removeNthFromEnd(node1,5)