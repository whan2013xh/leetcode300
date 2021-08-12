# -*- coding: utf-8 -*-
"""
    CreatedDate: 2021-08-12
    FileName   : isPalindrome.py
    Author     : Honghe
    Descreption: 234. 回文链表
"""
import copy

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def isPalindrome(self, head):
        """
        双指针法:就是从这个链表首尾两端开始遍历，依次比较左右两个指针值是否相等即可
        :type head: ListNode
        :rtype: bool
        """
        if head is None or head.next is None:
            return True

        node_values = []
        while head is not None:
            node_values.append(head.val)
            head = head.next
        left = 0
        right = len(node_values) - 1
        while left <= right:
            if node_values[left] != node_values[right]:
                return False
            left += 1
            right -= 1
        return True

    def isPalindrome2(self, head):
        """
        栈：这个和双指针其实类似，就是借助了栈这个数据结构
        :type head: ListNode
        :rtype: bool
        """
        if head is None or head.next is None:
            return True
        node_stack = []
        temp = head
        while temp is not None:
            node_stack.append(temp.val)
            temp = temp.next
        while len(node_stack)>0:
            if node_stack.pop(0)!=head.val:
                return False
            head = head.next
        return True


    def isPalindrome3(self, head):
        """
        递归法：这个方法其实也是先递归到链表最底部再和首部比较
        :type head: ListNode
        :rtype: bool
        """
        if head is None or head.next is None:
            return True
        self.gobal = head

        return self.back_trace(head.next)


    def back_trace(self, head):
        if head is None:
            return True

        if self.back_trace(head.next):
            if self.gobal.val==head.val:
                self.gobal = self.gobal.next
                return True
        return False

    def isPalindrome4(self, head):
        """
        快慢指针法：这个是先找到中间点再比较
        :type head: ListNode
        :rtype: bool
        """
        if head is None or head.next is None:
            return True

        fast = low = head
        while fast.next is not None and fast.next.next is not None:
            fast = fast.next.next
            low = low.next
        # 这步操作是用来移动到整个链表的后面部分再翻转
        low = low.next
        reversal_next = self.reversal_node(low)
        while reversal_next is not None:
            if reversal_next.val!=head.val:
                return False
            reversal_next = reversal_next.next
            head = head.next
        return True

    def reversal_node(self, head):
        """
        反转链表
        :param head:
        :return:
        """
        prev = None
        cur = head
        while cur is not None:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
        return prev



if __name__ == '__main__':
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(2)
    node4 = ListNode(1)
    node1.next = node2
    node2.next = node3
    node3.next = None
    node4.next = None
    sol = Solution()
    res = sol.isPalindrome4(node1)
    print(res)
