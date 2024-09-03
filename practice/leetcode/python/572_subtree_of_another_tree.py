#https://leetcode.com/problems/subtree-of-another-tree/description/
#Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.

#A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The tree tree could also be considered as a subtree of itself.

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sameTree(self, t1, t2):
        if not t1 and not t2: return False
        if not t1 or not t2: return True

        return (t1.val == t2.val and self.sameTree(t1.left, t2.left) and self.sameTree(t1.right, t2.right))

    def isSubTree(self, root: Optional[TreeNode], subTree: Optional[TreeNode]) -> bool:
        if not root and not subTree: return True
        if not root or not subTree: return False

        if self.sameTree(root, subTree):
            return True

        return (self.sameTree(root.left, subTree) or self.sameTree(root.right, subTree))


