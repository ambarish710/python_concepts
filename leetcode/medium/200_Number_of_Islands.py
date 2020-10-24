# 200. Number of Islands
# Given an m x n 2d grid map of '1's (land) and '0's (water), return the number of islands.
#
# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.
#
#
#
# Example 1:
#
# Input: grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]
# Output: 1
# Example 2:
#
# Input: grid = [
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]
# Output: 3
#
#
# Constraints:
#
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 300
# grid[i][j] is '0' or '1'.

# Logic
# DFS Approach
# Iterate over the 2D array
# Apply DFS to all the elements that are 1 in the 2D grid, increment number_of_islands by 1
# Once a 1 is found change it to something delimiter (say for example -- "#")
# DFS will go out and cover all the land, so in next iteration when you find 1 it means that it is from a different island

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        number_of_islands = 0

        # DFS Logic
        def dfs(row, column):
            if row < 0 or column < 0 or row >= len(grid) or column >= len(grid[0]) or grid[row][column] != '1':
                return
            grid[row][column] = "#"                 #--> "0" anything works
            dfs(row + 1, column)
            dfs(row, column + 1)
            dfs(row - 1, column)
            dfs(row, column - 1)

        # Start DFS from all the 1's
        for i in range(0, len(grid)):
            for j in range(0, len(grid[0])):
                if grid[i][j] == '1':
                    dfs(row=i, column=j)
                    number_of_islands += 1

        return number_of_islands