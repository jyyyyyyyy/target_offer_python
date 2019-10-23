# 给定一个double类型的浮点数base和int类型的整数exponent。求base的exponent次方。
# 保证base和exponent不同时为0
# -*- coding:utf-8 -*-
class Solution:
    def Power(self, base, exponent):
        res = 1;
        if base == 0:
            return 0
        if exponent == 0:
            return 0
        if(exponent < 0):
            for i in range(-exponent):
                res = res * base
            return 1/res
        else:
            for i in range(exponent):
                res = res * base
            return res