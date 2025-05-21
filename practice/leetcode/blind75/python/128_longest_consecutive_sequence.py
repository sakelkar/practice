from typing import List


class Solution:
    def longstConsecutive(self, nums):
        nums = set(nums)
        best = 0
        for x in nums:
            if x - 1 not in nums:
                y = x + 1
                while y in nums:
                    y += 1
                best = max(best, y - x)
        return(best)

    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set(nums)
        best = 0
        for x in numsSet:
            if x-1 not in numsSet:
                y = x + 1
                while y in numsSet:
                    y += 1
                best = max(best, y - x)
        return(best)

