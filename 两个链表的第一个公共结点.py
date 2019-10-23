#输入两个链表，找出它们的第一个公共结点。
# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        if not pHead1 and not pHead2:
            return None
        p1,p2 = pHead1,pHead2
        length1 = length2 = 0
        while p1:
            length1 += 1
            p1 = p1.next
        while p2:
            length2 += 1
            p2 = p2.next
        p1,p2 = pHead1,pHead2
        if length1 > length2:
            while length1-length2:
                p1 = p1.next
                length1 -= 1
        else:
            while length2-length1:
                p2 = p2.next
                length2 -= 1
        while p1 is not p2:
            p1=p1.next
            p2 = p2.next
        return p1
