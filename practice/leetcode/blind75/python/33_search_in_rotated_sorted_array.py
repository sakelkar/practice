#https://leetcode.com/problems/search-in-rotated-sorted-array/description/
from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binarySearch(nums, target, start, end):
            if start > end:
                return -1

            while (start <= end):
                mid = start + ((end - start) // 2)
                if nums[mid] == target:
                    return mid
                if nums[mid] < target:
                    start = mid + 1
                else:
                    end = mid - 1
            return -1

        l, r = 0, len(nums) - 1

        #first find the index of smallest element.
        while ((l < r) and (nums[l] > nums[r])):
            mid = (l + ((r - l) // 2))
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid

        pivot = l
        l, r = 0, len(nums) - 1
        if nums[pivot] <= target and target <= nums[r]:
            return(binarySearch(nums, target, pivot, r))
        else:
            return(binarySearch(nums, target, 0, pivot - 1))



