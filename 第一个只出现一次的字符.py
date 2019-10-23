# 在一个字符串(0<=字符串长度<=10000，全部由字母组成)中找到第一个只出现一次的字符,
# 并返回它的位置, 如果没有则返回 -1（需要区分大小写）
# -*- coding:utf-8 -*-
class Solution:
    #返回字符
    def FirstNotRepeatingChar(self, s):
        if s ==None :
            return -1
        dic = {}
        lists = list(s)
        for i in lists:
            if i not in dic.keys():
                dic[i] = 0
            dic[i] += 1
        for m in dic:
            if dic[m] == 1:
                return m
        return -1

 #返回字符的位置
    def FirstNotRepeatingChar(self, s):
        if s==None:
            return -1
        for i in s:
            if s.count(i)==1:
                return s.index()
                break
        return -1