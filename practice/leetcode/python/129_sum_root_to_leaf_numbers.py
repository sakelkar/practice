#https://leetcode.com/problems/sum-root-to-leaf-numbers/description/
#You are given the root of a binary tree containing digits from 0 to 9 only.
#Each root-to-leaf path in the tree represents a number.
#For example, the root-to-leaf path 1 -> 2 -> 3 represents the number 123.
#Return the total sum of all root-to-leaf numbers. Test cases are generated so that the answer will fit in a 32-bit integer.
#A leaf node is a node with no children.

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(root, sum):
            if root == None:
                return 0
            
            if root.left == None and root.right == None:
                return(sum*10+root.val)
            
            return(dfs(root.left, sum)+dfs(root.right, sum))

        return(dfs(root, 0))
