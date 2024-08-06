#https://leetcode.com/problems/longest-continuous-increasing-subsequence/description/
#Given an unsorted array of integers nums, return the length of the longest 
#continuous increasing subsequence (i.e. subarray). The subsequence must be strictly increasing.
#A continuous increasing subsequence is defined by two indices l and r (l < r) 
#such that it is [nums[l], nums[l + 1], ..., nums[r - 1], nums[r]] and for each l <= i < r, nums[i] < nums[i + 1].
from typing import List
class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        answer = 1
        running_answer = 1

        if len(nums) == 0 or len(nums) == 1:
            return len(nums)

        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                running_answer += 1
            else:
                answer = max(running_answer, answer)
                running_answer = 1
        return(max(answer, running_answer))

