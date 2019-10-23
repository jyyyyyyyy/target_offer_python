# -*- coding:utf-8 -*-
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None
class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        if not pHead:
            return None
        #复制每一个节点
        curnode = pHead
        while curnode:
            node = RandomListNode(curnode.label)
            node.next =  curnode.next
            curnode.next = node
            curnode = node.next
        #重新遍历链表，复制老结点的随机指针给新结点，如A1.random = A.random.next;
        curnode = pHead
        while curnode:
            node = curnode.next
            if curnode.random:
                node.random = curnode.random.next
            curnode = node.next
        #拆分, 将链表拆分为原链表和复制后的链表
        curnode = pHead
        copyHead = pHead.next
        while curnode.next:
            tmp = curnode.next
            curnode.next = tmp.next
            curnode = tmp
        return copyHead




