#https://leetcode.com/problems/binary-tree-postorder-traversal/description/
#Given the root of a binary tree, return the postorder traversal of its nodes' values.

from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def postOrderTraversal_Iterative(self, root: Optional[TreeNode]) -> List[int]:
        answer = []
        stack = []
        last = None
        while root or stack:
            if root:
                stack.append(root)
                root = root.left
            else:
                temp = stack.pop()
                if temp.right != None and temp.right != last:
                    root = temp.right
                else:
                    answer.append(temp.val)
                    last = temp
                    stack.pop()
        return(answer)


