
#输入n个整数，找出其中最小的K个数。例如输入4,5,1,6,2,7,3,8这8个数字，则最小的4个数字是1,2,3,4,。
# -*- coding:utf-8 -*-
class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        # 冒泡排序,到第k个数就停止
        if not tinput or k>len(tinput) or k<=0:
            return []
        for i in range(k):
            for j in range(i+1,len(tinput)):
                if tinput[j] < tinput[i]:
                    tinput[i],tinput[j] = tinput[j], tinput[i]
        return tinput[0:k]