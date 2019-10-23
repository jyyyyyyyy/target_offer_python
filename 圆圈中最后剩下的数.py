# -*- coding:utf-8 -*-
class Solution:
    def LastRemaining_Solution(self, n, m):
        if n < 1 or m<1:
            return -1
        cur = 0
        childnum = list(range(n))
        while len(childnum)>1:
            for i in range(1,m):
                cur += 1
                if cur == len(childnum):
                    cur = 0
            childnum.remove(childnum[cur])
            if cur == len(childnum):
                cur = 0
        return childnum[0]
