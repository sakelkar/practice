#https://leetcode.com/problems/longest-consecutive-sequence/description/
#Given an unsorted array of integers nums, return the length of 
#the longest consecutive elements sequence.
#You must write an algorithm that runs in O(n) time.
from typing import List


class Solution:
    def longestConsecutuveSequence(self, nums):
        nums = set(nums)
        best = 0

        for x in nums:
            while x - 1 not in nums:
                y = x + 1
                while y in nums:
                    y += 1
                best = max(best, y - x)
        return best

    def longestConsecutiveSequence(self, nums: List[int]) -> int:
        numsSet = set(nums)
        max_length = 0

        #for every num find whether its the smallest number if not then ignore it
        for num in nums:
            if (num - 1) in numsSet:
                continue

            #now you have found new smallest number now find its all consecutive numbers present in the list
            y = num + 1
            while y in nums:
                y += 1

            max_length = max(max_length, y - num)

        return max_length

