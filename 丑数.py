# 把只包含质因子2、3和5的数称作丑数（Ugly Number）。例如6、8都是丑数，但14不是，因为它包含质因子7。
# 习惯上我们把1当做是第一个丑数。求按从小到大的顺序的第N个丑数。
# -*- coding:utf-8 -*-
class Solution:
    def GetUglyNumber_Solution(self, index):
        if index == None or index<=0:
            return 0
        urgly=[0]*(index+1)
        idx2 = 1
        idx3 = 1
        idx5 = 1
        urgly[1]=1
        for i in range(2,index+1):
            new2 = urgly[idx2]*2
            new3 = urgly[idx3]*3
            new5 = urgly[idx5]*5
            urgly[i] = min(new2,new3,new5)
            if new2 == urgly[i]:
                idx2+=1
            if new3 == urgly[i]:
                idx3+=1
            if new5 == urgly[i]:
                idx5+=1
        return urgly[index]