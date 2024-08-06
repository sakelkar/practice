#https://leetcode.com/problems/merge-two-binary-trees/description

#You are given two binary trees root1 and root2.
#Imagine that when you put one of them to cover the other, some nodes of the two trees are 
#overlapped while the others are not. You need to merge the two trees into a new binary tree. 
#The merge rule is that if two nodes overlap, then sum node values up as the new value of the merged node. 
#Otherwise, the NOT null node will be used as the node of the new tree.
#Return the merged tree.
#Note: The merging process must start from the root nodes of both trees.
from types import _T2
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def mergeTrees(self, t1: Optional[TreeNode], t2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not t1:
            return t2
        if not t2:
            return t1
        else:
            res = TreeNode(t1.val+t2.val)
            res.left = self.mergeTrees(t1.left, t2.left)
            res.right = self.mergeTrees(t2.right, t2.right)
        return(res)

    def mergeTrees_BFS(self, t1: Optional[TreeNode], t2: Optional[TreeNode]) -> Optional[TreeNode]:
        if t1 == None:
            return t2
        if t2 == None:
            return t1

        stack = []
        stack = [[t1, t2]]
        while len(stack):
            node = stack.pop()
            if node[0] == None and node[1] == None:
                continue
            node[0].val += node[1].val
            if node[0].left and node[1].left:
                stack.append([node[0].left, node[1].left])
            elif node[1].left:
                node[0].left = node[1].left

            if node[0].right and node[1].right:
                stack.append([node[0].right, node[1].right])
            elif node[1].right:
                node[0].left = node[1].right
        return(t1)

            
