#定义栈的数据结构，请在该类型中实现一个能够得到栈中所含最小元素的min函数（时间复杂度应为O（1））。
# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.stack = []
        self.minlist = []
    def push(self, node):
        if not self.minlist:
            self.minlist.append(node)
        else:
            self.minlist.append(min(minlist[-1],node))
        self.stack.append(node)

    def pop(self):
        if not self.stack:
            return None
        else:
            self.minlist.pop()
            return self.stack.pop()
    def top(self):
        # write code here
        if not self.stack:
            return None
        else:
            return self.stack[-1]
    def min(self):
        if not self.minlist:
            return None
        else:
            return self.minlist[-1]

