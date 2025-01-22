##https://leetcode.com/problems/first-missing-positive/
#Given an unsorted integer array nums. Return the smallest positive integer that is not present in nums.
#You must implement an algorithm that runs in O(n) time and uses O(1) auxiliary space.
#Example 1:
#Input: nums = [1,2,0]
#Output: 3
#Explanation: The numbers in the range [1,2] are all in the array.
#
#Example 2:
#Input: nums = [3,4,-1,1]
#Output: 2
#Explanation: 1 is in the array but 2 is missing.
#
#Example 3:
#Input: nums = [7,8,9,11,12]
#Output: 1
#Explanation: The smallest positive integer 1 is missing.
#
#Constraints:
#
#    1 <= nums.length <= 105
#    -231 <= nums[i] <= 231 - 1
from typing import List
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        #first zero out all the useless numbers i.e. the numbers are less than 1 and greater than len(nums)
        length = len(nums)
        for i in range(len(nums)):
            if nums[i] <= 0 or nums[i] >= len(nums):
                nums[i] = 0
        #now the record the frequency of each number at its correct place
        for i in range(len(nums)):
            nums[nums[i]%length] += length

        #again scan the array and now return the first index whose value is 0
        for i in range(len(nums)):
            if nums[i]%length == 0:
                return i+1

        return length
