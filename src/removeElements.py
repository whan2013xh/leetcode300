# -*- coding: utf-8 -*-
"""
    CreatedDate: 2021-08-24
    FileName   : removeElements.py
    Author     : Honghe
    Descreption: 
"""
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        # 为什么要新建一个节点来指向head，是避免val对应的就是首节点
        res = ListNode(val-1)
        res.next = head
        cur = head
        prev = res
        while cur is not None:
            if cur.val!=val:
                prev = cur
                cur=cur.next
            else:
                next = cur.next
                prev.next = next
                cur = next
        return res.next

if __name__ == '__main__':
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    sol = Solution()
    res = sol.removeElements(node1, 1)
    print(res)