#https://leetcode.com/problems/majority-element/description/
#Given an array nums of size n, return the majority element.
#The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.
#Example 1:
#Input: nums = [3,2,3]
#Output: 3
#Example 2:
#Input: nums = [2,2,1,1,1,2,2]

from collections import defaultdict
from typing import DefaultDict, List


class Solution:
    def majorityElement_MooreVoting(self, nums: List[int]) -> int:
        maj_count = 0
        maj = 0

        for num in nums:
            if maj_count == 0:
                maj = num

            if num == maj:
                maj_count += 1
            else: 
                maj_count -= 1

        return maj

    def majorityElement_OLog(self, nums: List[int]) -> int:
        nums = sorted(nums)
        n = len(nums)
        return nums[n//2]

    def majorityElement_Hashmap(self, nums: List[int]) -> int:
        n = len(nums)
        map = defaultdict(int)

        for num in nums:
            map[num] += 1

        n = n//2

        for key, value in map.items():
            if value > n:
                return key

        return 0
