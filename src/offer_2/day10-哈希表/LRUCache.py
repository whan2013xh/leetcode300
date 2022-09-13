# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-06-15
    FileName   : LRUCache.py
    Author     : Honghe
    Descreption: 
"""
class Double_linked_list():
    def __init__(self,key,val,next=None,pre=None):
        self.key = key
        self.val = val
        self.next = next
        self.pre = pre


class LRUCache(object):
    def __init__(self, capacity):
        """
        哈希表+双向链表
        :type capacity: int
        """
        self.capacity = capacity
        self.head = Double_linked_list(0,0)
        self.tail = Double_linked_list(-1,-1)
        self.head.next = self.tail
        self.tail.pre = self.head
        self.cache = {}
        self.size = 0


    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.cache:
            node = self.cache.get(key)
            self.move_to_head(node)
            return node.val
        return -1


    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.cache:
            node = self.cache.get(key)
            node.val = value
            self.move_to_head(node)
        else:
            if self.size==self.capacity:
                delete_node = self.tail.pre
                self.cache.pop(delete_node.key)
                self.delete_tail_node()
                self.size-=1
            node = Double_linked_list(key,value)
            self.add_to_head(node)
            self.size+=1
            self.cache[key]=node
        return

    def delete_tail_node(self):
        self.tail.pre.pre.next = self.tail
        self.tail.pre = self.tail.pre.pre

    def add_to_head(self,node):
        self.head.next.pre = node
        node.next = self.head.next
        node.pre = self.head
        self.head.next = node

    def move_to_head(self,node):
        node.next.pre = node.pre
        node.pre.next = node.next
        node.next = self.head.next
        node.pre = self.head
        self.head.next.pre = node
        self.head.next = node


if __name__ == '__main__':
    capacity = 2
    sol = LRUCache(capacity)
    sol.put(1,1)
    sol.put(2, 2)
    print(sol.get(1))
    sol.put(3,3)
    print(sol.get(2))
    sol.put(4,4)
    print(sol.get(1))
    print(sol.get(3))
    print(sol.get(4))


