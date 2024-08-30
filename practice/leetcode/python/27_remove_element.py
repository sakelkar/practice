#https://leetcode.com/problems/remove-element/description/

from typing import List


class Solution:
    def removeElement(self, nums: List[int])-> int:
        k = 0
        for x in nums:
            if nums[k] != x:
                nums[k] = x
                k += 1
        return k

