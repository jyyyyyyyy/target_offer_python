# -*- coding:utf-8 -*-
class Solution:
    def StrToInt(self, s):
        if s == None or len(s) == 0:
            return 0
        flag = 0
        start = 0
        if s[0]=='+' or s[0]=='-':
            flag = 1
            start = 1
            if s[0]=='-':
                flag = 2
        else:
            start = 0
        num = 0
        for i in range(start,len(s)):
            if s[i]>='0' and s[i]<='9':
                num = num*10+int(s[i])
            else:
                return 0
        if flag == 2:
            num = -num
        return num