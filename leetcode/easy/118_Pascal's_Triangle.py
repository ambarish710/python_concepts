# Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.
#
#
# In Pascal's triangle, each number is the sum of the two numbers directly above it.
#
# Example:
#
# Input: 5
# Output:
# [
#      [1],
#     [1,1],
#    [1,2,1],
#   [1,3,3,1],
#  [1,4,6,4,1]
# ]


# Logic
# Defining Pascals Triangle and a temporary variable
# Corner case check
    # If numRows is less than 0
    # If numRows is less than 1
    # If numRows is less than 2
# Iterate till temporary variable less than numRows
    # Append [1,1]
    # Get the last row
    # Add elements from last row and insert it at correct position in the last appended row ([1,1])
    # return pascals_triangle

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # Defining Pascals Triangle and a temporary variable
        pascals_triangle = [[1], [1, 1]]
        i = 2

        # Corner case check
        if numRows <= 0:
            return []

        if numRows == 1:
            return [[1]]

        if numRows == 2:
            return pascals_triangle

        # Iterate till temporary variable less than numRows
        while i < numRows:
            pascals_triangle.append([1, 1])
            last_row = pascals_triangle[i - 1]
            for j in range(len(last_row) - 1):
                temp_val = last_row[j] + last_row[j + 1]
                pascals_triangle[-1].insert(j + 1, temp_val)
            i += 1

        return pascals_triangle