#https://leetcode.com/problems/3sum-closest/
#Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.
#Return the sum of the three integers.
#You may assume that each input would have exactly one solution.
from typing import List
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int :
        result = float("-infinity") 
        nums.sort()
        for i in range(len(nums) - 1):
            left = i+1
            right = len(nums) - 1
            while (left < right):
                sum = nums[i] + nums[left] + nums[right]
                if sum > target:
                    right -= 1
                elif sum < target:
                    left += 1
                else:
                    return sum

                if abs(sum - target) < abs(result - target):
                    result = sum
        return int(result)

