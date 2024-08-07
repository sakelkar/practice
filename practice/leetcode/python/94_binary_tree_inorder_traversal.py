#https://leetcode.com/problems/binary-tree-inorder-traversal/description/
#Given the root of a binary tree, return the inorder traversal 
#of its nodes' values.

from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal_Morris(self, root: Optional[TreeNode]) -> List[int]:
        answer = []
        if not root:
            return answer

        while root:
            if not root.left:
                answer.append(root.val)
                root = root.right
            else:
                pre = root.left
                while pre.right != None and pre.right != root:
                    pre = pre.right

                if pre.right == None:
                    pre.right = root
                    root = root.left
                else:
                    pre.right = None
                    answer.append(root.val)
                    root = root.right
        return(answer)


