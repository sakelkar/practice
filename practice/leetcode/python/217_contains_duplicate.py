#https://leetcode.com/problems/contains-duplicate/description/
#Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
from typing import List

class Solution:
    def containsDuplicateBruteForce(self, nums: List[int]) -> bool:
        n = len(nums)
        for i in range(n-1):
            for j in range(i+1, n):
                if nums[i] == nums[j]:
                    return True

    def containsDuplicate_LogN(self, nums: List[int]) -> bool:
        nums.sort()
        n = len(nums)
        for i in range(1, n):
            if nums[i] == nums[i - 1]:
                return True
        
        return False

    def containsDuplicateSet(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True

            seen.add(num)
        return False

    def containsDuplicateHashMap(self, nums: List[int]) -> bool:
        seen = {}
        for num in nums:
            if num in seen and seen[num] >= 1:
                return True
            seen[num] = seen.get(num, 0) + 1
        return False
