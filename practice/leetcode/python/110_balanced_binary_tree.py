#https://leetcode.com/problems/balanced-binary-tree/description/
#Given a binary tree, determine if it is #height-balanced

class Solution:
    def isBalancedBinaryTree(self, root):
        return self.Height(root) == -1
    def Height(self, root):
        if root is None: return 0

        left_height, right_height = self.Height(root.left), self.Height(root.right)
        if left_height == -1 or right_height == -1 or abs(left_height - right_height) > 1:
            return -1
        return max(left_height, right_height) + 1

