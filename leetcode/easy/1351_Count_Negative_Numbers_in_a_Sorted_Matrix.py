# Given a m x n matrix grid which is sorted in non-increasing order both row-wise and column-wise, return the number of negative numbers in grid.
#
#
#
# Example 1:
#
# Input: grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
# Output: 8
# Explanation: There are 8 negatives number in the matrix.
# Example 2:
#
# Input: grid = [[3,2],[1,0]]
# Output: 0
# Example 3:
#
# Input: grid = [[1,-1],[-1,-1]]
# Output: 3
# Example 4:
#
# Input: grid = [[-1]]
# Output: 1
#
#
# Constraints:
#
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 100
# -100 <= grid[i][j] <= 100
#
#
# Follow up: Could you find an O(n + m) solution?



# Logic
# Approach 1 (Brute Force - O(n^2))
    # Iterate over the matrix
        # But check when you get the first occurence
        # Coz from that point onwards everything else is -ve
        # So you update total occurence accordinly

# Approach 2 (Binary Search - O(mlog(n)))
    # Iterate over rows
        # Use binary search to find the leftmost -ve element
        # Coz from that point onwards everything else is -ve
        # So you update total occurence accordinly#

class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        # Approach 1 (Brute Force - O(n^2))
        total_negative_numbers = 0

        row_len = len(grid)
        col_len = len(grid[0])

        for i in range(row_len):
            for j in range(col_len):
                if grid[i][j] < 0:
                    total_negative_numbers += col_len - j
                    break

        return total_negative_numbers

        # Approach 2 (Binary Search - O(mlog(n)))
        total_negative_numbers = 0

        row_len = len(grid)
        col_len = len(grid[0])

        for i in range(row_len):
            low = 0
            high = col_len

            while low < high:
                mid = (low + high) // 2
                if grid[i][mid] < 0:
                    high = mid
                else:
                    low = mid + 1
            total_negative_numbers += col_len - low

        return total_negative_numbers