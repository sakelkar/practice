#https://leetcode.com/problems/subsets/description/
#Given an integer array nums of unique elements, return all possible
#subset (the power set).
#The solution set must not contain duplicate subsets. Return the solution in any order.

from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans, N = List[List[int]], len(nums)
        outer_iter = 2**N - 1

        while outer_iter:
            copy, i, subset = outer_iter, N - 1, List[int]
            while copy:
                if copy & 1:
                    subset.append(nums[i])
                i, copy = i - 1, copy >> 1

            ans.append(subset)
            outer_iter -= 1

        return(ans)
        

