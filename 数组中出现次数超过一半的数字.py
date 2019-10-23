# 数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。例如输入一个长度为9的数组{1,2,3,2,2,2,5,4,2}。
# 由于数字2在数组中出现了5次，超过数组长度的一半，因此输出2。如果不存在则输出0。
# -*- coding:utf-8 -*-

class Solution:

# 采用用户“分形叶”思路（注意到目标数 超过数组长度的一半，对数组同时去掉两个不同的数字，
# 到最后剩下的一个数就是该数字。如果剩下两个，那么这两个也是一样的，就是结果）
# ，在其基础上把最后剩下的一个数字或者两个回到原来数组中，将数组遍历一遍统计一下数字出现次数进行最终判断。
    def MoreThanHalfNum_Solution(self, numbers):
        if not numbers:
            return 0
        res = numbers[0]
        count = 1
        for i in range(1,len(numbers)):
            if numbers[i] == res:
                count+=1
            else:
                count -= 1
            if count == 0:
                res = numbers[i]
                count = 1
        count = 0
        for i in range(len(numbers)):
            if numbers[i] == res:
                count += 1
        return res if count >len(numbers)/2.0 else 0