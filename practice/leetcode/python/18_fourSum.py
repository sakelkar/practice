#https://leetcode.com/problems/4sum/

#Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

#    0 <= a, b, c, d < n
#    a, b, c, and d are distinct.
#   nums[a] + nums[b] + nums[c] + nums[d] == target
#You may return the answer in any order.
from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        result, quad = [], []
        def kSum(k, start, target):
            if k != 2:
                for i in range(start, len(nums) - k + 1):
                    if i > start and nums[i] == nums[i-1]:
                        continue
                    quad.append(nums[i])
                    kSum(k - 1, i + 1, target - nums[i])
                    quad.pop()
                return
            #base case of twosum
            left, right = start + 1, len(nums) - 1
            while (left < right):
                if target > nums[left] + nums[right]:
                    right -= 1
                elif target < nums[left] + nums[right]:
                    left += 1
                else:
                    result.append(quad + [nums[left], nums[right]])
                    left += 1
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
            return
        kSum(4, 0, target)
        return result

