# -*- coding:utf-8 -*-
class Solution:
    def FindContinuousSequence(self, tsum):
        allres = []
        low ,high = 1, 2
        while(low < high):
