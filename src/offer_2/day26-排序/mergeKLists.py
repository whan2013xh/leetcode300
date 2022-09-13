# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-07-05
    FileName   : mergeKLists.py
    Author     : Honghe
    Descreption: 剑指 Offer II 078. 合并排序链表
"""
from typing import List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        """
        顺序合并
        :param lists:
        :return:
        """
        length = len(lists)
        head = None
        for i in range(length):
            head = self.merge(head, lists[i])
        return head

    def merge(self,head1,head2):
        if not head1 or not head2:
            return head1 if head1 else head2
        res = ListNode(0)
        cur = res
        while head1 and head2:
            if head1.val>head2.val:
                cur.next = head2
                head2=head2.next
            else:
                cur.next = head1
                head1 = head1.next
            cur = cur.next
        if head1:
            cur.next = head1
        if head2:
            cur.next = head2
        return res.next

    def mergeKLists2(self, lists):
        """
        归并排序，两两合并排序
        :param lists:
        :return:
        """
        res = self.merge_sort(lists,0,len(lists)-1)
        return res

    def merge_sort(self, lists, start, end):
        if start>end:
            return None
        if start==end:
            return lists[start]
        mid = (end-start)//2+start
        left = self.merge_sort(lists,start,mid)
        right = self.merge_sort(lists, mid+1,end)
        return self.merge(left,right)

    def mergeKLists3(self, lists):
        """
        优先权队列,先遍历链表数组的每一个链表的第一个节点，插入到优先权队列中，然后每次取出的时候再把这条链表中的下一个节点插入
        其实保存的的是每条链表的指针，只是借助优先权队列做好了排序
        :param lists:
        :return:
        """
        import heapq
        node_heapq=[]
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(node_heapq,(lists[i].val,i))
                lists[i]=lists[i].next

        res = ListNode(0)
        cur = res
        while node_heapq:
            val, index = heapq.heappop(node_heapq)
            cur.next = ListNode(val)
            cur = cur.next
            if lists[index]:
                heapq.heappush(node_heapq, (lists[index].val, index))
                lists[index] = lists[index].next
        return res.next





if __name__ == '__main__':
    sol = Solution()
    lists = [[1,4,5],[1,3,4],[2,6]]
    res = []
    for i in lists:
        head = ListNode(0)
        pre = head
        for index,j in enumerate(i):
            node = ListNode(j)
            pre.next = node
            pre = node
        res.append(head.next)

    print(sol.mergeKLists3(res))