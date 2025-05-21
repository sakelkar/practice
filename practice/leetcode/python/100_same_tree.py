from typing import Optional


class TreeNode:
    def __init__ (self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sameTree(self, t1: Optional[TreeNode], t2: Optional[TreeNode]) -> bool:
        if not t1 and not t2: return True
        if not t1 or not t2: return False

        return(t1.val == t2.val and self.sameTree(t1.left, t2.left) and self.sameTree(t1.right, t2.right))


class Solution2:
    def sameTree(self, t1: Optional[TreeNode], t2: Optional[TreeNode]) -> bool:
        if not t1 and not t2: return True
        if not t1 or not t1: return False

        return(t1.val == t2.val and self.sameTree(t1.left, t2.left) and self.sameTree(t1.right, t2.right))
