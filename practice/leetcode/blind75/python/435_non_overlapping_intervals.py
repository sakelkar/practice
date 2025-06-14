#Given an array of intervals intervals where intervals[i] = [starti, endi], return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.
#Note that intervals which only touch at a point are non-overlapping. For example, [1, 2] and [2, 3] are non-overlapping.
#
#Example 1:
#
#Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
#Output: 1
#Explanation: [1,3] can be removed and the rest of the intervals are non-overlapping.
#
#Example 2:
#
#Input: intervals = [[1,2],[1,2],[1,2]]
#Output: 2
#Explanation: You need to remove two [1,2] to make the rest of the intervals non-overlapping.
#
#Example 3:
#
#Input: intervals = [[1,2],[2,3]]
#Output: 0
#Explanation: You don't need to remove any of the intervals since they're already non-overlapping.
from typing import List

class Solution:
    def nonOverlappingIntervals(self, intervals: List[List[int]]) -> int:
        end, cnt = float('-inf'), 0
        for s, e in sorted(intervals, key=lambda x: x[1]):
            if s >= end:
                end = e
            else:
                cnt += 1
        return cnt

    def eraseOverlappingInterval(self, intervals: List[List[int]]) -> int:
        end, cnt = float('-inf'), 0
        for s, e in sorted(intervals, key=lambda x: x[1]):
            if s >= end:
                end = e
            else:
                cnt += 1
        return cnt
