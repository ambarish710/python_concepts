# Given a square matrix mat, return the sum of the matrix diagonals.
#
# Only include the sum of all the elements on the primary diagonal and all the elements on the secondary diagonal that are not part of the primary diagonal.
#
#
#
# Example 1:
#
#
# Input: mat = [[1,2,3],
#               [4,5,6],
#               [7,8,9]]
# Output: 25
# Explanation: Diagonals sum: 1 + 5 + 9 + 3 + 7 = 25
# Notice that element mat[1][1] = 5 is counted only once.
# Example 2:
#
# Input: mat = [[1,1,1,1],
#               [1,1,1,1],
#               [1,1,1,1],
#               [1,1,1,1]]
# Output: 8
# Example 3:
#
# Input: mat = [[5]]
# Output: 5
#
#
# Constraints:
#
# n == mat.length == mat[i].length
# 1 <= n <= 100
# 1 <= mat[i][j] <= 100


# Logic
# Run for loops in two direction
    # One incrementing
    # Other decrementing
# Return the sum of diagonals


class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        mat_len = len(mat)
        diagonal_total = 0

        for i, j in zip(range(mat_len), range(mat_len - 1, -1, -1)):
            if i == j:
                diagonal_total += mat[i][i]
            else:
                diagonal_total += mat[i][i] + mat[i][j]

        return diagonal_total
