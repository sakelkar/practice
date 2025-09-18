#Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.
#
#Example 1:
#
#Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
#Output: [3,9,20,null,null,15,7]
#
#Example 2:
#
#Input: preorder = [-1], inorder = [-1]
#Output: [-1]
#
#Constraints:
#    1 <= preorder.length <= 3000
#    inorder.length == preorder.length
#    -3000 <= preorder[i], inorder[i] <= 3000
#    preorder and inorder consist of unique values.
#    Each value of inorder also appears in preorder.
#    preorder is guaranteed to be the preorder traversal of the tree.
#    inorder is guaranteed to be the inorder traversal of the tree.

#preorder: root, left, right
#inorder: left, root, right

from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None

        root_val = preorder[0]
        root = TreeNode(root_val)
        mid = inorder.index(root_val)

        #recursive call
        root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])

        return root

    def buildTree2(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        #construct the inorder map for index fetching quickly
        inorder_map = { val:i for i, val in enumerate(inorder)}
        self.pre_idx = 0

        def helper(left, right):
            if left > right:
                return None

            #first fetch from preorder as the current root
            root_val = preorder[self.pre_idx]
            self.pre_idx += 1
            root = TreeNode(root_val)

            #find the mid from inorder_map
            mid = inorder_map[root_val]

            root.left = helper(left, mid - 1)
            root.right = helper(mid+1, right)

            return root

        return helper(0, len(inorder) - 1)

