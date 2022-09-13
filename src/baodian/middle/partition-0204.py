# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-08-23
    FileName   : partition-0204.py
    Author     : Honghe
    Descreption: 
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        new_head = ListNode(0)
        new_head.next = head
        pre = new_head
        cur = head
        pos = 0
        while cur is not None:
            # 先找打大于x的节点
            if cur.val<x and pos==0:
                pre = cur
                cur = cur.next
                continue
            pos=1
            if cur.val<x:
                pre.next = cur.next
                cur.next = new_head.next
                new_head.next = cur
                cur = pre.next
            else:
                pre = cur
                cur = cur.next
        return new_head.next

if __name__ == '__main__':
    sol = Solution()
    head = [3,1]
    nodes = []
    for i in head:
        tmp = ListNode(i)
        if nodes:
           nodes[-1].next = tmp
        nodes.append(tmp)
    x = 2
    sol.partition(nodes[0],x)
    print(nodes)
