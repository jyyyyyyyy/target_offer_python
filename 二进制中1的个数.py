#输入一个整数，输出该数二进制表示中1的个数。其中负数用补码表示。
# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1(self, n):
        if n < 0:
            n = n & 0xffffffff #得到正数
        count = 0
        while n:
            count += 1
            n = n & (n-1)
        return count
        # write code here