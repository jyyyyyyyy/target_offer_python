# 输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有的奇数位于数组的前半部分，
# # 所有的偶数位于数组的后半部分，并保证奇数和奇数，偶数和偶数之间的相对位置不变。
# -*- coding:utf-8 -*-
class Solution:
    def reOrderArray(self, array):
        for i in range(len(array)-1):
            if array[i] % 2 ==0 and array[i+1] % 2 == 1:
                array[i],array[i+1]=array[i+1],array[i]
            while i > 0:
                if array[i] % 2 == 1 and array[i - 1] % 2 == 0:
                    array[i-1], array[i] = array[i], array[i-1]
                i -= 1
        return array
