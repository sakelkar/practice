from typing import List


class Solution:
    def longstConsecutive(self, nums):
        nums = set(nums)
        best = 0
        for x in nums:
            if x - 1 not in nums:
                y = x + 1
                while y in nums:
                    y += 1
                best = max(best, y - x)
        return(best)
    def longestConsecutive(self, nums):
        nums = set(nums)
        best = 0
        for x in nums:
            if x - 1 not in nums:
                y = x + 1
                while y in nums:
                    y += 1
                best = max(best, y - x)
        return(best)
    def longestConsecutiveSorting(self, nums: List[int]):
        if not nums:
            return 0

        nums.sort()

        longest_streak = 1
        current_streak = 1

        for i in range(1, len(nums)):
            #take care of the duplicates
            if nums[i] == nums[i-1]:
                continue

            if nums[i] == nums[i-1] + 1:
                current_streak += 1
            else:
                current_streak = 1

            longest_streak = max(longest_streak, current_streak)

        return longest_streak

    def longest_consecutive_stream(self, nums: List[int]):
        lengths = {}
        longest = 0

        for n in nums:
            if n in lengths:
                continue

            left_len = lengths.get(n - 1, 0)
            right_len = lengths.get(n + 1, 0)
            total_len = left_len + 1 + right_len
            lengths[n] = total_len
            longest = max(total_len, longest)

            #update the start of streak at n - 1
            lengths[n - left_len] = total_len
            #update the start of streak at n + 1
            lengths[n + right_len] = total_len



