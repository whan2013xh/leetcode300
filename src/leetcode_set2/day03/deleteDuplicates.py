# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-04-08
    FileName   : deleteDuplicates.py
    Author     : Honghe
    Descreption: 82. 删除排序链表中的重复元素 II
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return head
        new_node = ListNode()
        new_node.next = head
        pre = new_node
        cur = head
        next_node = cur.next
        flag = False
        while cur and next_node:
            if cur.val == next_node.val:
                next_node = next_node.next
                flag = True
            else:
                if flag:
                    pre.next = next_node
                    flag = False
                else:
                    pre = cur
                cur = next_node
                next_node = next_node.next
        if flag:
            pre.next = None
        return new_node.next


