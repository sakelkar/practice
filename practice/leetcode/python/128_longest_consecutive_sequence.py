#https://leetcode.com/problems/longest-consecutive-sequence/description/
#Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
#You must write an algorithm that runs in O(n) time.
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
