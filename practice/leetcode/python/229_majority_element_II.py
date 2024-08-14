##//https://leetcode.com/problems/majority-element-ii/description/
##//Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.
##//Example 1:
##//Input: nums = [3,2,3]
##//Output: [3]
##//Example 2:
##//Input: nums = [1]
##//Output: [1]
##//Example 3:
##//Input: nums = [1,2]
##//Output: [1,2]
from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        if not nums:
            return []

        m1, m2, cm1, cm2 = 0, 0, 0, 0

        for num in nums:
            if num == m1:
                cm1 += 1
            elif num == m2:
                cm2 += 1
            elif cm1 == 0:
                m1 = num
                cm1 += 1
            elif cm2 == 0:
                m2 = num
                cm2 += 1
            else:
                cm1 -= 1
                cm2 -= 1

        #By now m1 and m2 would have been identified
        #so check their count
        return [num for num in (m1, m2) if nums.count(num) > len(nums) // 3]
