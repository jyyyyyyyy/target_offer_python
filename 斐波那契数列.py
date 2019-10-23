'''大家都知道斐波那契数列，现在要求输入一个整数n，请你输出斐波那契数列的第n项（从0开始，第0项为0）。n<=39'''
# -*- coding:utf-8 -*-
class Solution:
    def Fibonacci(self, n):
        array = [0,1,1,2]
        while len(array) <= n:
            array.append(array[-1] + array[-2])
        return  array[n]
        # write code here
