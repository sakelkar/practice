#https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/description/
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def lowestCommonAncestor(self, root: Optional[TreeNode], p: Optional[TreeNode], q: Optional[TreeNode]) -> int:
        if not root: return 0
        if not p and not q: return 0
        if not p or not q: return 0
        while (root.val - p.val) * (root.val - q.val) > 0:
            root = (root.left, root.right)[p.val > root.val]
        return root

    def lowestCommonAncestor2(self, root: Optional[TreeNode], p: Optional[TreeNode], q: Optional[TreeNode]) -> int:
        while root:
            if p.val < root.val and q.val < root.val:
                root = root.left
            elif p.val > root.val and q.val > root.val:
                root = root.right
            else:
                return root
