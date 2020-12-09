# Given a n x n matrix where each of the rows and columns are sorted in ascending order, find the kth smallest element in the matrix.
#
# Note that it is the kth smallest element in the sorted order, not the kth distinct element.
#
# Example:
#
# matrix = [
#    [ 1,  5,  9],
#    [10, 11, 13],
#    [12, 13, 15]
# ],
# k = 8,
#
# return 13.
# Note:
# You may assume k is always valid, 1 ≤ k ≤ n2.


# Logic
# Conver the matrix into a flat list
# Sort the flat list
# And return the value at the kth position



class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        flat_list = []
        for row in matrix:
            flat_list += row
        flat_list.sort()
        return flat_list[k-1]