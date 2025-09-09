#Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.
#
#Example 1:
#Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
#Output: [[1,6],[8,10],[15,18]]
#Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
#
#Example 2:
#Input: intervals = [[1,4],[4,5]]
#Output: [[1,5]]
#Explanation: Intervals [1,4] and [4,5] are considered overlapping.
#
#Example 3:
#Input: intervals = [[4,7],[1,4]]
#Output: [[1,7]]
#Explanation: Intervals [1,4] and [4,7] are considered overlapping.
#
#Constraints:
#    1 <= intervals.length <= 104
#    intervals[i].length == 2
#    0 <= starti <= endi <= 104

from typing import List


class Solution:
    def mergeIntervals(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals or len(intervals[0]) == 0:
            return []

        answer = []
        #sort the intervals array first in asending order of first element
        intervals.sort(key=lambda x:x[0])
        answer.append(intervals[0])

        for start, end in intervals[1:]:
            last_end = answer[-1][1]
            if start <= last_end:
                answer[-1][1] = max(last_end, start)
            else:
                answer.append([start, end])
        return answer

