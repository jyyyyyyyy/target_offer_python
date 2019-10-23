#输入一棵二叉树，求该树的深度。从根结点到叶结点依次经过的结点（含根、叶结点）形成树的一条路径，最长路径的长度为树的深度。

# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:

    def TreeDepth(self, pRoot):
        if pRoot == None:
            return 0
        return self.levelOrder(pRoot)
    #层次遍历
    def levelOrder(self, root):
        count = 0# 统计层数
        if root == None:
            return count
        q = [] # 模拟一个队列储存节点
        q.append(root)  # 首先将根节点入队
        while len(q) != 0:   # 列表为空时，循环终止，说明没有新的叶子节点层
            length = len(q)#记录同层次结点的个数
            for i in range(length):
                head = q.pop(0)  # 将同层节点依次出队
                if head.left:
                    q.append(head.left)
                if head.right:
                    q.append(head.right)
            count += 1

        return count
