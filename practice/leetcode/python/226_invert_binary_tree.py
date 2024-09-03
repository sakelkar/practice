#https://leetcode.com/problems/invert-binary-tree/description/
#Given the root of a binary tree, invert the tree, and return its root.
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root 

        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root: 
            return None

        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)

    def invertTree_iterative(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root

        stack = [root]
        while (len(stack)):
            node = stack.pop()
            node.left, node.right = node.right, node.left
            if node.left: 
                stack.append(node.left)
            if node.right:
                stack.append(node.right)

        return(root)

    def invertTree_iterative(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        st = [root]
        while (len(st)):
            node = st.pop()
            node.left, node.right = node.right, node.left
            if node.left:
                st.append(node.left)
            if node.right:
                st.append(node.right)
        return(root)
        

