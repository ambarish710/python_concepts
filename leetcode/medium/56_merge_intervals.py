# Given a collection of intervals, merge all overlapping intervals.
#
# Example 1:
#
# Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
# Example 2:
#
# Input: intervals = [[1,4],[4,5]]
# Output: [[1,5]]
# Explanation: Intervals [1,4] and [4,5] are considered overlapping.
# NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Covering Corner Case
        if len(intervals) < 2:
            return intervals

        # Non-overlap List to return
        non_overlap_list = []

        def myfunc(x):
            return x[0], x[1]

        intervals.sort(key=myfunc)

        for interval in intervals:
            if not non_overlap_list or non_overlap_list[-1][1] < interval[0]:
                non_overlap_list.append(interval)
            else:
                non_overlap_list[-1][1] = max(non_overlap_list[-1][1], interval[1])

        return non_overlap_list
