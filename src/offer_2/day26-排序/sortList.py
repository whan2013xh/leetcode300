# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-07-04
    FileName   : sortList.py
    Author     : Honghe
    Descreption: 
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head:
            return head
        cur = head
        node = ListNode(float("-inf"))
        node.next=head
        pre = node
        step = 0
        while cur:
            next = cur.next
            step+=1
            if next and next.val<cur.val:
                cur.next = next.next
                for i in range(step):
                    tmp = pre
                    pre = pre.next
                    if pre.val>next.val:
                        tmp.next = next
                        next.next=pre
                        pre = node
                        break
            else:
                cur = cur.next
        return node.next

    def sortList2(self, head):
        """
        归并算法,自顶向下
        :param head:
        :return:
        """
        if not head:
            return head
        res = self.split_list(head,None)
        return res


    def split_list(self,head,tail):
        length = 0
        cur = head
        while cur!=tail:
            length += 1
            cur = cur.next
        if length==1:
            return head

        mid = head
        for i in range(length//2-1):
            mid = mid.next
        mid_head = mid.next
        mid.next = None
        head1 = self.split_list(head,None)
        head2 = self.split_list(mid_head,tail)
        res = self.merge(head1,head2)
        return res

    def merge(self,list1,list2):
        head = ListNode(0)
        list3 = head
        while list1 and list2:
            if list1.val>list2.val:
                list3.next = list2
                list2 = list2.next
            else:
                list3.next = list1
                list1 = list1.next
            list3 = list3.next
        if list1:
            list3.next=list1
        if list2:
            list3.next = list2
        return head.next

    def sortList3(self, head):
        """
        归并算法,字底向上,每次将链表切分成长度为1，2，4，。。这样的链表合并
        :param head:
        :return:
        """
        if not head:
            return head
        length = 0
        cur = head
        while cur:
            length += 1
            cur = cur.next

        step = 1
        res = ListNode(0,head)

        while step<length:
            pre, cur = res, res.next
            while cur:
                head1 = cur
                for i in range(step-1):
                    if cur:
                        cur = cur.next
                    else:
                        break
                if cur:
                    head2 = cur.next
                    cur.next = None
                    cur = head2
                else:
                    head2 = cur
                for i in range(step-1):
                    if cur:
                        cur = cur.next
                    else:
                        break

                if cur:
                    next = cur.next
                    cur.next = None
                    cur = next


                pre.next = self.merge(head1,head2)
                while pre.next:
                    pre = pre.next
            step = step*2
        return res.next


if __name__ == '__main__':
    nums = [-1,5,3,4,0]
    res = []
    for i in nums:
        node = ListNode(i)
        if res:
           res[-1].next=node
        res.append(node)
    sol = Solution()
    print(sol.sortList3(res[0]))







