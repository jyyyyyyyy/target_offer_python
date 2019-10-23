#输入一棵二叉树，判断该二叉树是否是平衡二叉树。
#-*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def IsBalanced_Solution(self, pRoot):
        if pRoot == None:
            return True
        if abs(self.getDepth(pRoot.left)-self.getDepth(pRoot.right))>1:
            return False
        return self.IsBalanced_Solution(pRoot.left) and self.IsBalanced_Solution(pRoot.right)
    def getDepth(self, pRoot):
        if pRoot == None:
            return 0
        left = self.getDepth(pRoot.left)
        right = self.getDepth(pRoot.right)
        return max(left,right)+1
