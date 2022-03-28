# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-03-17
    FileName   : copyRandomList.py
    Author     : Honghe
    Descreption: 
"""
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return

        cache_nodes = {}
        cur = head
        while cur:
            cache_nodes[cur] = Node(cur.val)
            cur = cur.next

        cur = head
        while cur:
            cache_nodes[cur].next = cache_nodes.get(cur.next)
            cache_nodes[cur].random = cache_nodes.get(cur.random)
            cur = cur.next
        return cache_nodes.get(head)


