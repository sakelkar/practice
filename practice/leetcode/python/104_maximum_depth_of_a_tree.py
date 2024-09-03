from typing import Optional


class TreeNode:
    def __init__ (self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0

        q = deque([root])
        lvl = 0

        while len(q):
            for _ in range(len(q)):
                temp = q.popleft()
                if temp.left: q.append(temp.left)
                if temp.right: q.append(temp.right)
            lvl += 1
        return lvl

