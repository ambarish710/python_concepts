# Given a matrix A, return the transpose of A.
#
# The transpose of a matrix is the matrix flipped over it's main diagonal, switching the row and column indices of the matrix.
#
#
#
#
#
# Example 1:
#
# Input: [[1,2,3],[4,5,6],[7,8,9]]
# Output: [[1,4,7],[2,5,8],[3,6,9]]
# Example 2:
#
# Input: [[1,2,3],[4,5,6]]
# Output: [[1,4],[2,5],[3,6]]
#
#
# Note:
#
# 1 <= A.length <= 1000
# 1 <= A[0].length <= 1000

# Logic
# Since the matrix is n*m and not n*n
# We go by a different approach than transpose of n*n matrix
# First we create a temp matrix whose rows are = size of cols in original matrix and cols are = that of rows
# Then iterate over the matrix and fill it

class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        t_matrix = [[0] * len(A) for i in range(len(A[0]))]

        for r, row in enumerate(A):
            for c, col in enumerate(row):
                t_matrix[c][r] = col

        return t_matrix