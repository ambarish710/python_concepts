# Given an m x n binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.
#
#
#
# Example 1:
#
#
# Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
# Output: 4
# Example 2:
#
#
# Input: matrix = [["0","1"],["1","0"]]
# Output: 1
# Example 3:
#
# Input: matrix = [["0"]]
# Output: 0
#
#
# Constraints:
#
# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 300
# matrix[i][j] is '0' or '1'.



# Logic
# Create a matrix with size one extra on height and in width
# Assign 0 as values of that matrix
# Iterate over the new created matrix starting 1,1 till end
# if original matrix's current value is 1
    # Then take the min of all the values on top, left corner, left of the reference matrix
    # Add one to it
    # Update the ref matrix current value with it
    # Keep the size value updated with the max in the ref matrix
# Return size ** 2




class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if len(matrix) == 0:
            return 0

        size = 0

        ref_matrix = [[0] * (len(matrix[0]) + 1) for i in range(len(matrix) + 1)]

        for i in range(1, len(matrix) + 1):
            for j in range(1, len(matrix[0]) + 1):
                if matrix[i - 1][j - 1] == "1":
                    ref_matrix[i][j] = min(ref_matrix[i - 1][j], ref_matrix[i][j - 1], ref_matrix[i - 1][j - 1]) + 1
                    size = max(ref_matrix[i][j], size)

        return size ** 2