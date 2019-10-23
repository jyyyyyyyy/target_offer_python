#一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个n级的台阶总共有多少种跳法（先后次序不同算不同的结果）。
# -*- coding:utf-8 -*-
class Solution:
    def jumpFloor(self, number):
        array = [1,1,2]
        while len(array) < number:
            array.append(array[-1]+array[-2])
        return array[number]
