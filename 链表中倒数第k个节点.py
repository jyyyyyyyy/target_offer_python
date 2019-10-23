#输入一个链表，输出该链表中倒数第k个结点。
# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def FindKthToTail(self, head, k):
        if head == None or k <= 0:
            return None
        slow = head #设置两个指针，p2指针先走（k-1）步，然后再一起走，当p2为最后一个时，p1就为倒数第k个 数
        fast = head
        while k > 1:#p2先走，走k-1步，如果k大于链表长度则返回 空，否则的话继续走
            if fast.next != None:
                fast = fast.next
            else:
                return None
            k -= 1
        while fast.next != None:#两个指针一起 走，一直到p2为最后一个,p1即为所求
            fast = fast.next
            slow = slow.next
        return slow