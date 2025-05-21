from typing import List


class Solution:
    def maxSubArraySum(self, nums: List[int]) -> int:
        curr_max, maximum = 0, 0
        for c in nums:
            curr_max = max(c, curr_max + c)
            maximum = max(maximum, curr_max)
        return maximum
