
#https://leetcode.com/problems/subsets-ii/description/
#Given an integer array nums that may contain duplicates, return all possible
#subsets (the power set).
#The solution set must not contain duplicate subsets. Return the solution in any order.
#Example 1:
#Input: nums = [1,2,2]
#Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
#Example 2:
#Input: nums = [0]

from typing import List

class Solution:
    def subsetWithDup_Backtracking(self, nums: List[int]) -> List[List[int]]:
        def dfs(curr, nums):
            result.append(curr)

            if len(nums) == 0:
                return
                
            for i in range(len(nums)):
                if i > 0 and nums[i] == nums[i-1]:
                    continue
                dfs(curr + [nums[i]], nums[i+1:])

        result = []
        dfs([], sorted(nums))
        return(result)

    def subsetWithDup_Backtracking2(self, nums: List[int]) -> List[List[int]]:
        def dfs(idx: int, curr: List[int]):
            answer.append(curr)

            for i in range(idx, len(curr)):
                if i > idx and nums[i] == nums[i-1]:
                    continue

                curr.append(nums[i])
                dfs(i+1, curr)
                curr.pop()

        answer = []
        nums.sort()
        dfs(0, [])
        return(answer)

    def subsetWithDup_Backtracking3(self, nums: List[int]) -> List[List[int]]:
        def dfs(self, res, start, subset, nums):
            res.append(list[subset])

            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i-1]:
                    continue
                subset.append(nums[i])
                dfs(self, res, i+1, subset, nums)
                subset.pop()

        nums = sorted(nums)
        res = []
        dfs(self, res, 0, [], nums)
        return res

    def subsetWithDup_Backtracking4(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums = sorted(nums)

        def dfs(self, res, nums, idx, subset):
            res.append(list(subset))

            for i in range(idx, len(nums)):
                if i > idx and nums[i] == nums[i-1]:
                    continue
                subset.append(nums[i])
                dfs(self, res, nums, i+1, subset)
                subset.pop()

        dfs(self, res, nums, 0, [])
        return(res)
