#https://leetcode.com/problems/product-of-array-except-self/description/
from typing import List
import math

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if nums.count(0) > 1: return [0] * len(nums)

        prod = math.prod(nums)

        product_without_zero = 1
        for num in nums:
            if num == 0: continue
            product_without_zero *= num

        answer = []
        for num in nums:
            if num == 0:
                answer.append(product_without_zero)
            else:
                answer.append(prod//num)

        return(answer)
