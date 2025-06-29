#https://leetcode.com/problems/longest-increasing-subsequence/

#Given an integer array nums, return the length of the longest strictly increasing subsequence

from typing import List
from bisect import bisect_left

class Solution:
    def lengthofLIS(self, nums: List[int]) -> int:
        LIS = [1] * len(nums)
        for i in range (len(nums)):
            for j in range (i+1, len(nums)):
                if nums[i] < nums[j]:
                    LIS[i] = max(LIS[i], 1 + LIS[j])
        return(max(LIS))

    def lengthOfLIS2(self, nums: List[int]) -> int:
        LIS = [1] * len(nums)
        #range start, stop, step
        for i in range(len(nums)-1, -1, -1):
            for j in range(i+1, len(nums)):
                if nums[j] > nums[i]:
                    nums[i] = max(nums[i], 1 + nums[j])
        return max(LIS)

    def lengthOfLIS3(self, nums: List[int]) -> int:
        sub = []
        for x in nums:
            if len(sub) == 0 or sub[-1] < x:
                sub.append(x)
            else:
                idx = bisect_left(sub, x)
                sub[idx] = x
        return len(sub)

