#https://leetcode.com/problems/longest-increasing-subsequence/

#Given an integer array nums, return the length of the longest strictly increasing subsequence

from typing import List

class Solution:
    def lengthofLIS(self, nums: List[int]) -> int:
        LIS = [1] * len(nums)
        for i in range (len(nums)):
            for j in range (i+1, len(nums)):
                if nums[i] < nums[j]:
                    LIS[i] = max(LIS[i], 1 + LIS[j])
        return(max(LIS))
