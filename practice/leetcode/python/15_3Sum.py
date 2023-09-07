#https://leetcode.com/problems/3sum/
#Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
#Notice that the solution set must not contain duplicate triplets.

#Basic logic
#Boundary conditions
#Check the length < 3 return []
#Sort
#Check if the first number > 0 after sorting return []

#Create a hashMap[] and update the highest index for the given value of the number

#for loop to find first non-repeating number
#run 2nd for loop to find second non-repeating number
#negate the sum of find1 and find2
#search in hashMap above and insert into list of lists
#return

from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for index, value in enumerate(nums):
            if index > 0 and value == nums[index+1]:
                continue

            left, right = index + 1, len(nums)
            while (left < right):
                threeSum = value + nums[left] + nums[right]
                if threeSum > 0:
                    right -= 1
                elif threeSum < 0:
                    left += 1
                else:
                    res.append([value, nums[left], nums[right]])
                    left += 1
                    while left < right and nums[left - 1] == nums[left]:
                        left += 1
        return(res)
