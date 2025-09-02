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

    def search2(self, nums: List[int], target: int) -> int:
        def binarySearch(nums, target, start, end):
            if start > end:
                return -1
            while (start < end):
                mid = start + ((end - start)//2)
                if nums[mid] == target:
                    return mid
                if nums[mid] < target:
                    start = mid + 1
                else:
                    end = mid - 1
            return -1

        l, r = 0, len(nums) - 1
        while (l < r):
            mid = l + (r - l)//2
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid
        # this is the index of min element of the list
        pivot = l
        #search from this index to end if target falls in that range
        #else search in 0 to this index - 1 range
        if nums[pivot] <= target and nums[r] >= target:
            return(binarySearch(nums, target, pivot, r))
        else:
            return(binarySearch(nums, target, 0, pivot-1))

    def search3(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l, r = 0, n - 1
        while l < r:
            mid = (l + r) // 2
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid

        pivot = l
        l, r = 0, n - 1
        while l <= r:
            mid = (l + r)//2
            real_mid = (mid + pivot)%n
            if nums[real_mid] == target:
                return real_mid
            elif nums[real_mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return -1
