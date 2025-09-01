from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for index, value in enumerate(nums):
            diff = target - value
            if diff in map:
                return[map[diff], index]
            map[value] = index

        return[]

    def twoSum2(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for index, value in enumerate(nums):
            diff = target - value
            if diff in map:
                return[map[diff], index]
            map[value] = index
        return []

    def twoSum5(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for index, value in enumerate(nums):
            diff = target - value
            if diff in map:
                return [map[diff], index]
            map[value] = index
        return []

    def twoSum6(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for index, value in enumerate(nums):
            diff = target - value
            if diff in map:
                return([map[diff], index])
            map[value] = index
        return []
