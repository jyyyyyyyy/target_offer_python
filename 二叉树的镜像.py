#操作给定的二叉树，将其变换为源二叉树的镜像。
# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回镜像树的根节点
    #递归方法
    def Mirror(self, root):
        if root == None:
            return None
        if root.left == None and root.right == None:
            return root
        tmp = root.left
        root.left = root.right
        root.right = tmp
        self.Mirror(root.left)
        self.Mirror(root.right)

    #非递归方法
    def Mirror2(self, root):
        if root == None:
            return None
        if root.left == None and root.right == None:
            return root
        nodeque = [root]
        while len(nodeque)>0:
            curlen, count = len(nodeque), 0
            while count < curlen:
                count += 1
                pRoot = nodeque.pop(0)#把第一个元素弹出
                pRoot.left, pRoot.right = pRoot.right, pRoot.left
                if pRoot.left:
                    nodeque.append(pRoot)
                if pRoot.right:
                    nodeque.append(pRoot.right)




