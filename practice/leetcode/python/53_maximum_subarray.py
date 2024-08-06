#https://leetcode.com/problems/maximum-subarray/description/
#Given an integer array nums, find the subarray
#with the largest sum, and return its sum.
from typing import List

class Solution:
    def maxSubArraySum(self, nums: List[int]) -> float: 
        maxSum = float('-inf')
        currentSum = 0

        for num in nums:
            currentSum += num
            if currentSum > maxSum:
                maxSum = currentSum

            if currentSum < 0:
                currentSum = 0
        return(maxSum)
