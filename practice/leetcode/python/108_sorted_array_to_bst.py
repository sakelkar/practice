#https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/description/
#Given an integer array nums where the elements are sorted in ascending order, convert it to a
#height-balanced
#binary search tree.

class TreeNode:
    def __init__ (self, val=0, left=None, right=None):
        self.val = 0
        self.left = left
        self.right = right

class Solution:
    def sortedArrayToBst(self, nums):
        def recurse(start, end):
            if end < start:
                return None

            mid = start + (end - start)/2
            root = TreeNode(nums[mid])
            root.left = recurse(start, mid)
            root.right = recurse(mid+1, end)
            return(root)
            
        return(recurse(0, len(nums)-1))
