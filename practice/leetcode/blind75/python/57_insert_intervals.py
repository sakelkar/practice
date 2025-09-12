#You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. You are also given an interval newInterval = [start, end] that represents the start and end of another interval.
#Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).
#Return intervals after the insertion.
#Note that you don't need to modify intervals in-place. You can make a new array and return it.
#
#Example 1:
#Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
#Output: [[1,5],[6,9]]
#
#Example 2:
#Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
#Output: [[1,2],[3,10],[12,16]]
#Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
#
#Constraints:
#    0 <= intervals.length <= 104
#    intervals[i].length == 2
#    0 <= starti <= endi <= 105
#    intervals is sorted by starti in ascending order.
#    newInterval.length == 2
#    0 <= start <= end <= 105

from typing import List

class Solution:
    def insertInterval(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals or len(intervals[0]):
            return newInterval

        #start with a new empty list
        #intervals is already sorted. so fill all the intervlas before newInterval start into the new list
        new = []
        n = list(intervals)
        i = 0

        #1. first fill all the intervals in intervals input which are smaller than newInterval
        while i < n and intervals[i][1] < newInterval[0]:
            new.append(intervals[i])
            i += 1

        #when you come here then if i < n then intervals[i][1] > newInterval[0]
        #i.e. the current interval end is > newInterval start
        #so the overalap ends when current interval start is > newInterval end
        #so until newInterval end is >= current interval start keep merging
        #all the intervals and make it as new interval

        #2. merge all the intervals in intervals and newInterval as applicable
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(intervals[i][0], newInterval[0])
            newInterval[1] = max(intervals[i][1], newInterval[1])
            i += 1
        new.append(newInterval)

        while i < n:
            new.append(intervals[i])
            i += 1

        return(new)
