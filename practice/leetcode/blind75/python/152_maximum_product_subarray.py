from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        A = nums
        B = A[::-1]

        for i in range(1, len(A)):
            A[i] *= A[i-1] or 1
            B[i] *= B[i-1] or 1

        return max(A + B)

    def maxProduct2(self, nums: List[int]) -> int:
        A = nums
        B = A[::-1]
        for i in range(1, len(A)):
            A[i] *= A[i-1] or 1
            B[i] *= B[i-1] or 1

        return(max(A+B))

    def maxProductSimple(self, nums: List[int]) -> int:
        prefix, suffix, max_so_far = 0, 0, 0

        for i in range(len(nums)):
            prefix = prefix or 1 * nums[i]
            suffix = suffix or 1 * nums[len(nums)-i]
            max_so_far = max(max_so_far, prefix, suffix)

        return(max_so_far)

    def maxProductSimple2(self, nums: List[int]) -> int:
        prefix, suffix, max_so_far = 0, 0, 0
        for i in range(len(nums)):
            prefix = prefix or 1 * nums[i]
            suffix = suffix or 1 * nums[~1]
            max_so_far = max(max_so_far, prefix, suffix)
        return(max_so_far)

    def maxProductSimple3(self, nums: List[int]) -> int:
        prefix, suffix, max_so_far = 0, 0, float('-inf')
        for i in range(len(nums)):
            prefix = (prefix or 1) * nums[i]
            suffix = (suffix or 1) * nums[~i]
            max_so_far = max(max_so_far, prefix, suffix)
        return(max_so_far)

    def maxProduct3(self, nums: List[int]) -> int:
        A = nums
        B = nums[::-1]
        for i in range(1, len(A)):
            A[i] *= A[i-1] or 1
            B[i] *= B[i-1] or 1

        #at the end of for loop, A and B contain prefix product and suffix product
        return(max(A+B))
