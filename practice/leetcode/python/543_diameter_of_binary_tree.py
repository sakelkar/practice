#https://leetcode.com/problems/diameter-of-binary-tree/description/
#Given the root of a binary tree, return the length of the diameter of the tree.
#The diameter of a binary tree is the length of the longest path between any two nodes in a tree. 
#This path may or may not pass through the root.
#The length of a path between two nodes is represented by the number of edges between them.

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def diameter(node, res):
            if node is None:
                return 0

            left = diameter(node.left, res)
            right = diameter(node.right, res)

            res = max(res, left + right)

            return 1 + max(left, right)
        
        res = 0
        diameter(root, res)
        return(res)

