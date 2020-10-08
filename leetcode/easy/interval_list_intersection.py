# Given two lists of closed intervals, each list of intervals is pairwise disjoint and in sorted order.
#
# Return the intersection of these two interval lists.
#
# (Formally, a closed interval [a, b] (with a <= b) denotes the set of real numbers x with a <= x <= b.  The intersection of two closed intervals is a set of real numbers that is either empty, or can be represented as a closed interval.  For example, the intersection of [1, 3] and [2, 4] is [2, 3].)
#
# Example
# 1:
#
# Input: A = [[0, 2], [5, 10], [13, 23], [24, 25]], B = [[1, 5], [8, 12], [15, 24], [25, 26]]
# Output: [[1, 2], [5, 5], [8, 10], [15, 23], [24, 24], [25, 25]]

class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        ans = []
        i = j = 0

        while i < len(A) and j < len(B):
            # Let's check if A[i] intersects B[j].
            # lo - the startpoint of the intersection
            # hi - the endpoint of the intersection
            lo = max(A[i][0], B[j][0])
            hi = min(A[i][1], B[j][1])
            if lo <= hi:
                ans.append([lo, hi])

            # Remove the interval with the smallest endpoint
            if A[i][1] < B[j][1]:
                i += 1
            else:
                j += 1

        return ans


# Doesn't work
# return_list = []
#
# if not A or not B:
#     return return_list
#
# for i in range(0, len(A) - 1):
#     if A[i][1] >= B[i][0]:
#         sublist = [B[i][0], A[i][1]]
#         if sublist not in return_list:
#             return_list.append(sublist)
#
#     if A[i][1] >= B[i + 1][0]:
#         sublist = [B[i + 1][0], A[i][1]]
#         if sublist not in return_list:
#             return_list.append(sublist)
#
#     if B[i][1] >= A[i + 1][0]:
#         sublist = [A[i + 1][0], B[i][1]]
#         if sublist not in return_list:
#             return_list.append(sublist)
#
#     if A[i + 1][1] >= B[i + 1][0]:
#         sublist = [B[i + 1][0], A[i + 1][1]]
#         if sublist not in return_list:
#             return_list.append(sublist)
#
# return return_list


# def intersection(A, B):
#     result = []
#     i, j = 0, 0
#
#     while i < len(A) and j < len(B):
#         # Let's check if A[i] intersects B[j].
#         # lo - the startpoint of the intersection
#         # hi - the endpoint of the intersection
#         low = max(A[i][0], B[j][0])
#         high = min(A[i][1], B[j][1])
#
#         if low <= high:
#             result.append([low, high])
#
#         # Remove the interval with the smallest endpoint
#         if A[i][1] < B[j][1]:
#             i += 1
#         else:
#             j += 1
#
#     return result