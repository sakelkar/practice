#https://leetcode.com/problems/symmetric-tree/description/
#Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).
from typing import Optional

class TreeNode:
    def __init__ (self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def dfs(left, right):
            if left == None or right == None:
                return left == right
            if left.val == right.val:
                return(dfs(left.left, right.right) and dfs(left.right, right.left))
            return False

        return(root == None or dfs(root.left, root.right))
