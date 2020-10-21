# 240. Search a 2D Matrix II
# Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:
#
# Integers in each row are sorted in ascending from left to right.
# Integers in each column are sorted in ascending from top to bottom.
# Example:
#
# Consider the following matrix:
#
# [
#   [1,   4,  7, 11, 15],
#   [2,   5,  8, 12, 19],
#   [3,   6,  9, 16, 22],
#   [10, 13, 14, 17, 24],
#   [18, 21, 23, 26, 30]
# ]
# Given target = 5, return true.
#
# Given target = 20, return false.

# Logic
# The logic is to first find out the correct column and then find the row
# Initialize the col as last element row as first row
# Start from the endmost column value in the first row
# Check if target less than value, go to the point till find correct column
# Then just increment row. If the target not in that column its not in the 2d matrix
# If yes col -= 1

class Solution:
    def searchMatrix(self, matrix, target):
        if matrix == []:
            return False

        col = len(matrix[0]) - 1
        row = 0

        while col >= 0 and row < len(matrix):
            if target == matrix[row][col]:
                return True
            elif target < matrix[row][col]:
                col -= 1
            elif target > matrix[row][col]:
                row += 1

        return False