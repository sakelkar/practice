from typing import List


class Solution:
    def maxSubArraySum(self, nums: List[int]) -> int:
        curr_max, maximum = 0, 0
        for c in nums:
            curr_max = max(c, curr_max + c)
            maximum = max(maximum, curr_max)
        return maximum

    def maxSubArraySum1(self, nums: List[int]) -> int:
        curr_max, abs_max = 0, 0
        for n in nums:
            curr_max = max(curr_max, n + curr_max)
            abs_max = max(abs_max, curr_max)
        return abs_max

    def maxSubArraySum2(self, nums: List[int]) -> int:
        curr_max, abs_max = 0, 0
        for n in nums:
            curr_max = max(curr_max, curr_max + n)
            abs_max = max(abs_max, curr_max)
        return abs_max

    def maxSubArraySum3(self, nums: List[int]) -> int:
        curr_max, abs_max = nums[0], nums[0]
        #in python range function is half open that is left is inclusive and right is exclusive
        for i in range(1, len(nums)):
            curr_max = max(curr_max, nums[i] + curr_max)
            abs_max = max(abs_max, curr_max)
        return abs_max
