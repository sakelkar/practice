#Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.
#
#Example 1:
#Input: nums = [3,0,1]
#Output: 2
#Explanation:
#n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the range since it does not appear in nums.
#
#Example 2:
#Input: nums = [0,1]
#Output: 2
#Explanation:
#n = 2 since there are 2 numbers, so all numbers are in the range [0,2]. 2 is the missing number in the range since it does not appear in nums.
#
#Example 3:
#Input: nums = [9,6,4,2,3,5,7,0,1]
#Output: 8
#Explanation:
#n = 9 since there are 9 numbers, so all numbers are in the range [0,9]. 8 is the missing number in the range since it does not appear in nums.
#
#Constraints:
#    n == nums.length
#    1 <= n <= 104
#    0 <= nums[i] <= n
#    All the numbers of nums are unique.
from typing import List


class Solution:
    def missinNumber(self, nums: List[int]) -> int:
        #so if the list has n elements then the list can have number [0, n].
        #pls note that 0, n are actually n+1 numbers but list is of size n. hence the missing number
        #so what we can do is that, we can do running sum of i and subtract running sum nums[i]
        #the differnce at the end of the loop is the missing number
        index_sum = 0
        value_sum = 0
        result = 0
        for i in range(len(nums)):
            index_sum += i
            value_sum += nums[i]

        result = value_sum - index_sum
        return(result)

    def missingNumber2(self, nums: List[int]) -> int:
        n = len(nums)
        theory_sum = n * (n + 1) // 2
        actual = sum(nums)
        return theory_sum - actual

    def missingNumer3(self, nums: List[int]) -> int:
        nums.sort()
        for i, num in enumerate(nums):
            if i != num:
                return i
        return(len(nums))



