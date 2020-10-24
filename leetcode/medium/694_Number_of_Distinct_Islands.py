# 694. Number of Distinct Islands
# Medium
#
# 954
#
# 58
#
# Add to List
#
# Share
# Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.
#
# Count the number of distinct islands. An island is considered to be the same as another if and only if one island can be translated (and not rotated or reflected) to equal the other.
#
# Example 1:
# 11000
# 11000
# 00011
# 00011
# Given the above grid map, return 1.
# Example 2:
# 11011
# 10000
# 00001
# 11011
# Given the above grid map, return 3.
#
# Notice that:
# 11
# 1
# and
#  1
# 11
# are considered different island shapes, because we do not consider reflection / rotation.
# Note: The length of each dimension in the given grid does not exceed 50.


# Logic
# DFS -- Same logic as number of islands
# The only difference is the following, we send a string while making a recursive dfs call
# X - While starting DFS
# O - Out of bounds or Zero
# U - Up
# R - Right
# D - Down
# L - Left
# And keep this entire big string in a set, this represents a shape (post entire dfs iteration)
# And return the shape set len, this will inform you about the number of distinct islands
# TC -- O(M*N)
# SC -- O(M*N)


class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        if len(grid) == 0:
            return 0

        number_of_distinct_islands = set()

        def dfs(grid, row, col, direction):
            if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]) or grid[row][col] != 1:
                return "O"
            grid[row][col] = "O"
            up = dfs(grid, row + 1, col, "U")
            right = dfs(grid, row, col + 1, "R")
            down = dfs(grid, row - 1, col, "D")
            left = dfs(grid, row, col - 1, "L")
            return (direction + up + right + down + left)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    path = dfs(grid, i, j, "X")
                    number_of_distinct_islands.add(path)

        return len(number_of_distinct_islands)