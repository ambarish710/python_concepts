# Given the availability time slots arrays slots1 and slots2 of two people and a meeting duration duration, return the earliest time slot that works for both of them and is of duration duration.
#
# If there is no common time slot that satisfies the requirements, return an empty array.
#
# The format of a time slot is an array of two elements [start, end] representing an inclusive time range from start to end.
#
# It is guaranteed that no two availability slots of the same person intersect with each other. That is, for any two time slots [start1, end1] and [start2, end2] of the same person, either start1 > end2 or start2 > end1.
#
#
#
# Example 1:
#
# Input: slots1 = [[10,50],[60,120],[140,210]], slots2 = [[0,15],[60,70]], duration = 8
# Output: [60,68]
# Example 2:
#
# Input: slots1 = [[10,50],[60,120],[140,210]], slots2 = [[0,15],[60,70]], duration = 12
# Output: []
#
#
# Constraints:
#
# 1 <= slots1.length, slots2.length <= 10^4
# slots1[i].length, slots2[i].length == 2
# slots1[i][0] < slots1[i][1]
# slots2[i][0] < slots2[i][1]
# 0 <= slots1[i][j], slots2[i][j] <= 10^9
# 1 <= duration <= 10^6



# Logic
# First of all remove all entities whose difference is greater than the duration
# Sort both the lists
# Create 2 pointers i and j and initialize to 0
# Iterate over both lists till i and j are less than len of both the lists
# Check if intervals1[i][1] <= intervals2[j][0]:
        # i += 1
# Check if intervals2[j][1] <= intervals1[i][0]:
        # j += 1
# Find start: max or 0's and end: min of 1's
# Append output
# Sort output and return 0th position




class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:

        output = []
        i, j = 0, 0

        # Approach 1
        def filter_unreq(slot):
            interval = []
            for sl in slot:
                if sl[1] - sl[0] >= duration:
                    interval.append(sl)
            return interval

        intervals1 = filter_unreq(slots1)
        intervals2 = filter_unreq(slots2)

        intervals1.sort()
        intervals2.sort()

        # Approach 2
        # intervals1 = sorted(filter(lambda x: x[1] - x[0] >= duration, slots1))
        # intervals2 = sorted(filter(lambda x: x[1] - x[0] >= duration, slots2))

        while i < len(intervals1) and j < len(intervals2):
            if intervals1[i][1] <= intervals2[j][0]:
                i += 1
                continue
            if intervals2[j][1] <= intervals1[i][0]:
                j += 1
                continue
            start = max(intervals1[i][0], intervals2[j][0])
            end = start + duration
            if end <= min(intervals1[i][1], intervals2[j][1]):
                output.append([start, end])
            i += 1
            j += 1

        output.sort()
        if output:
            return output[0]
        else:
            return []
