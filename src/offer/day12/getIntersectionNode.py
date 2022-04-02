# -*- coding: utf-8 -*-
"""
    CreatedDate: 2022-04-01
    FileName   : getIntersectionNode.py
    Author     : Honghe
    Descreption: 剑指 Offer 52. 两个链表的第一个公共节点
"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        """
        两种方案：
        1、交叉遍历，A遍历完了就遍历B，B遍历完了遍历A，则两个相等的节点就是相遇的点
        2、首尾相连，构成环
        :param headA:
        :param headB:
        :return:
        """
        if not (headA and headB):
            return None
        pos1 = headA
        pos2 = headB
        count1 = 0
        count2 = 0
        while pos1 and pos2:
            if pos1==pos2:
                return pos1
            pos1 = pos1.next
            pos2 = pos2.next
            if not pos1:
                if count1==0:
                    pos1 = headB
                    count1+=1
                else:
                    return None
            if not pos2:
                if count2==0:
                    count2+=1
                    pos2 = headA
                else:
                    return None


        return None

    def getIntersectionNode2(self, headA: ListNode, headB: ListNode) -> ListNode:
        """
        两种方案：
        1、交叉遍历，A遍历完了就遍历B，B遍历完了遍历A，则两个相等的节点就是相遇的点
        2、首尾相连，构成环
        :param headA:
        :param headB:
        :return:
        """
        if not (headA and headB):
            return None
        pos1 = headA
        pos2 = headB

        while pos1 != pos2:
            pos1 = pos1.next if pos1 else headB
            pos2 = pos2.next if pos2 else headA
        return pos1





