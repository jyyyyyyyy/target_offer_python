#输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。如果是则输出Yes,否则输出No。假设输入的数组的任意两个数字都互不相同。
# -*- coding:utf-8 -*-
class Solution:
    def VerifySquenceOfBST(self, sequence):
        if sequence == None or len(sequence)==0:
            return False
        length = len(sequence)
        root = sequence[length - 1]
        for i in range(length):
            if sequence[i] > root:
                break
        for j in range(i,length):
            if sequence[j] < root:
                return False
        left = True
        if i > 0:
            left = self.VerifySquenceOfBST(sequence[0:i])
        right = True
        if i < length - 1:
            right = self.VerifySquenceOfBST(sequence[i:-1])
        return left and right
