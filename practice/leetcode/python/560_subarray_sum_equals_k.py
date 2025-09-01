#https://leetcode.com/problems/subarray-sum-equals-k/description/
#Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.
#A subarray is a contiguous non-empty sequence of elements within an array.
#Example 1:
#Input: nums = [1,1,1], k = 2
#Output: 2
#Example 2:
#Input: nums = [1,2,3], k = 3
#Output: 2
#Constraints:
#    1 <= nums.length <= 2 * 104
#    -1000 <= nums[i] <= 1000
#    -107 <= k <= 107
from typing import List
from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if sum(nums[i:(j+1)]) == k:
                    count += 1
        return count

    def subarraySum2(self, nums: List[int], k: int) -> int:
        prefix_sum_freq = defaultdict(int)
        count = 0
        curr_sum = 0

        prefix_sum_freq[0] = 1

        for num in nums:
            curr_sum += num
            count += prefix_sum_freq[curr_sum - k]
            prefix_sum_freq[curr_sum] += 1

        return count
