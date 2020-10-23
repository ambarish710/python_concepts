# In a given grid, each cell can have one of three values:
#
# the value 0 representing an empty cell;
# the value 1 representing a fresh orange;
# the value 2 representing a rotten orange.
# Every minute, any fresh orange that is adjacent (4-directionally) to a rotten orange becomes rotten.
#
# Return the minimum number of minutes that must elapse until no cell has a fresh orange.  If this is impossible, return -1 instead.
#
#
#
# Example 1:
#
#
#
# Input: [[2,1,1],[1,1,0],[0,1,1]]
# Output: 4
# Example 2:
#
# Input: [[2,1,1],[0,1,1],[1,0,1]]
# Output: -1
# Explanation:  The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.
# Example 3:
#
# Input: [[0,2]]
# Output: 0
# Explanation:  Since there are already no fresh oranges at minute 0, the answer is just 0.
#
#
# Note:
#
# 1 <= grid.length <= 10
# 1 <= grid[0].length <= 10
# grid[i][j] is only 0, 1, or 2.
# Accepted
# 167,154
# Submissions
# 338,298


# Logic -- BFS
# First traverse through the 2D matrix and put rotten oranges index positions in the queue
# And count the number of fresh oranges
# Flood fill approach from all rotten oranges, that is take first rotten orange do a flood fill till you can and then move to next
# Change adjacent fresh to rotten orange and add to queue
# Also make sure to add a sentinel once a level ends (sentinel is nothing but a digit or char)




from queue import Queue

#994. Rotting Oranges
class Solution:
    def orangesRotting(self, grid):
        sentinel = [-1]
        queue = Queue()
        queue.put(sentinel)
        seconds_elapsed, fresh_oranges_count = 0, 0
        row_len, col_len = len(grid), len(grid[0])

        # Put rotten oranges in queue and count fresh oranges
        for i in range(0, row_len):
            for j in range(0, col_len):
                if grid[i][j] == 1:
                    fresh_oranges_count += 1
                elif grid[i][j] == 2:
                    queue.put([i, j])

        # LOGIC
        # Flood approach from all rotten oranges and check if fresh orange count can come down to zero
        while queue.qsize() > 1 and fresh_oranges_count > 0:
            orange_index = queue.get()
            if orange_index[0] == -1:
                seconds_elapsed += 1
                queue.put(sentinel)
            else:
                rindex, cindex = orange_index[0], orange_index[1]
                for new_rindex, new_cindex in ((rindex-1, cindex), (rindex, cindex-1), (rindex+1, cindex), (rindex, cindex+1)):
                    if 0 <= new_rindex < row_len and 0 <= new_cindex < col_len and grid[new_rindex][new_cindex] == 1:
                        fresh_oranges_count -= 1
                        grid[new_rindex][new_cindex] = 2
                        queue.put([new_rindex, new_cindex])

        if fresh_oranges_count == 0:
            return seconds_elapsed
        else:
            return -1

