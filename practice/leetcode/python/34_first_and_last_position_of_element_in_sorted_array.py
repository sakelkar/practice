##https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description
#Given an array of integers nums sorted in non-decreasing order, find the starting and ending position
#of a given target value
#If target is not found in the array, return [-1, -1]
#You must write an algorithm with O(log n) runtime complexity
#Example 1:

#Input: nums = [5,7,7,8,8,10], target = 8
#Output: [3,4]
#Example 2:

#Input: nums = [5,7,7,8,8,10], target = 6
#Output: [-1,-1]
#Example 3:

#Input: nums = [], target = 0
#Output: [-1,-1]

from typing import List
from bisect import bisect_left


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l = bisect_left(nums, target)
        r = bisect_left(nums, target+1)
        return [-1, -1] if l == r else [l, r-1]