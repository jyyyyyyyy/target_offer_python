# 输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的双向链表。
# 要求不能创建任何新的结点，只能调整树中结点指针的指向。
# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def Convert(self, pRootOfTree):
        if not pRootOfTree:
            return None
        if not pRootOfTree.left and not pRootOfTree.right:
            return pRootOfTree

        left = self.Convert(pRootOfTree.left)
        p = left
        # 定位至左子树的最右的一个结点
        while left and p.right:
            p = p.right

        # 如果左子树不为空，将当前root加到左子树链表
        if left:
            p.right = pRootOfTree
            pRootOfTree.left = p

        right = self.Convert(pRootOfTree.right)
        if right:
            right.left = pRootOfTree
            pRootOfTree.right = right

        return left if left else pRootOfTree

    #非递归中序遍历
    def Convert1(self, pRootOfTree):
        if not pRootOfTree:
            return None
        stack = []
        restack = []
        p = pRootOfTree
        while p or stack:
            if p:
                stack.append(p)
                p = p.left
            else:
                node = stack.pop()
                restack.append(node)
                p = node.right

        proot = restack[0]
        while restack:
            top = restack.pop(0)
            if restack:
                top.right=restack[0]
                restack[0].left=top
        return proot