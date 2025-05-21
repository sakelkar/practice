#https://leetcode.com/problems/binary-tree-level-order-traversal/description/
#Given the root of a binary tree, return the level order traversal of its nodes' values. 
#(i.e., from left to right, level by level).
from typing import Optional
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        answer: List[List[int]] = []
        queue = []
        queue.append(root)

        while len(queue) > 0:
            level = []
            for _ in range(len(queue)):
                node = queue.pop(0)
                level.append(node.val)
                if (node.left):
                    queue.append(node.left)
                if (node.right):
                    queue.append(node.right)

            answer.append(level)
        return(answer)

    def levelOrder2(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        answer = List[List[int]] = []
        queue = []
        queue.append(root)

        while len(queue):
            level = []
            for _ in range(len(queue)):
                node = queue.pop(0)
                level.appned(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            answer.append(level)
        return(answer)

    def levelOrder3(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        answer = []
        queue = []
        queue.append(root)

        while len(queue):
            level = []
            for _ in range(len(queue)):
                node = queue.pop(0)
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            answer.append(level)
        return(answer)
