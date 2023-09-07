#https://leetcode.com/problems/container-with-most-water/

#You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
#Find two lines that together with the x-axis form a container, such that the container contains the most water.
#Return the maximum amount of water a container can store.
#Notice that you may not slant the container.
from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        maxArea = 0
        while (left < right):
            maxArea = max(maxArea, (right - left) * min(height[left], height[right]))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return(maxArea)

class Solution2:
    def maxArea(self, height: List[int]) -> int:
        maxA = 0
        left, right = 0, len(height) - 1
        while (left < right):
            maxA = max(maxA, ((right - left) * min(height[left], height[right])))
            if height[left] < height[right]:
                left += 1
            else:
                right += 1
        return(maxA)
 
