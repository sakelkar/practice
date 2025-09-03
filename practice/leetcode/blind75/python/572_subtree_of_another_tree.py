#Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same
#structure and node values of subRoot and false otherwise.
#A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants.
#The tree tree could also be considered as a subtree of itself.

from typing import Optional
from hashlib import sha256

class TreeNode:
    def __init__(self, left: None, right: None, val: int, merkle: str):
        self.left = left
        self.right = right
        self.val = val
        self.merkle = merkle


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isMatch(root, subRoot):
            if not root or not subRoot:
                return root == subRoot
            if root.val == subRoot.val:
                return (isMatch(root.left, subRoot.left) and isMatch(root.right, subRoot.right))

        if isMatch(root, subRoot):
            return True

        return isMatch(root.left, subRoot) or isMatch(root.right, subRoot)

    def isSubtree2(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isMatch(root, subRoot):
            if not (root and subRoot):
                return root == subRoot
            return (root.val == subRoot.val) and (isMatch(root.left, subRoot.left)) and (isMatch(root.right, subRoot.right))

        def dfs(root, subRoot):
            if not (root and subRoot):
                return False
            return isMatch(root, subRoot) or dfs(root.left, subRoot.left) or dfs(root.right, subRoot.right)

        return dfs(root, subRoot)


    def isSubTree3(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isMatch(root, subRoot):
            if not (root and subRoot):
                return root == subRoot

            return root.left == subRoot.right and isMatch(root.left, subRoot.left) and isMatch(root.right, subRoot.right)

        def dfs(root, subRoot):
            if not root:
                return False

            return isMatch(root, subRoot) or dfs(root.left, subRoot) or dfs(root.right, subRoot)

        return dfs(root, subRoot)

    
    def isSubTree4(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isMatch(root, subRoot):
            if not (root and subRoot):
                return root == subRoot

            return root.val == subRoot.val and isMatch(root.left, subRoot.left) and isMatch(root.right, subRoot.right)

        def dfs(root, subRoot):
            if not (root and subRoot):
                return root == subRoot

            return isMatch(root, subRoot) or dfs(root.left, subRoot) or dfs(root.right, subRoot)

        return dfs(root, subRoot)

    def isSubTree5(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def serialize(root):
            if not root:
                return '#'
            return f"{serialize(root.left)},{root.val},{serialize(root.right)},"

        return serialize(subRoot) in serialize(root)

    def isSubtree(self, root: Optional[TreeNode], subroot: Optional[TreeNode]) -> bool:
        #return False if root is nil and subroot is not nil
        if not root and subroot:
            return False

        #return True if subroot is nil
        if not subroot:
            return False

        def isMatch(root, subroot):
            if not root:
                return False

            return root.val == subroot.val and isMatch(root.left, subroot.left) and isMatch(root.right, subroot.right)

        def dfs(root, subroot):
            if not root:
                return False

            isMatch(root, subroot) or dfs(root.left, subroot) or dfs(root.right, subroot)

        return(dfs(root, subroot))



class Solution2:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def hash_(x):
            S = sha256()
            S.update(x)
            return S.hexdigest()


        def merkle(node):
            if not node:
                return
            node.merkle = hash_(node.left + str(node.val) + node.right)
            #return node.merkle

        merkle(root)
        merkle(subRoot)

        def dfs(root):
            if not root:
                return False
            return(root.merkle == subRoot.merkle or dfs(root.left) or dfs(root.right))

        dfs(root)



