# There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b, and city b is connected directly with city c, then city a is connected indirectly with city c.
#
# A province is a group of directly or indirectly connected cities and no other cities outside of the group.
#
# You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.
#
# Return the total number of provinces.
#
#
#
# Example 1:
#
#
# Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
# Output: 2
# Example 2:
#
#
# Input: isConnected = [[1,0,0],[0,1,0],[0,0,1]]
# Output: 3
#
#
# Constraints:
#
# 1 <= n <= 200
# n == isConnected.length
# n == isConnected[i].length
# isConnected[i][j] is 1 or 0.
# isConnected[i][i] == 1
# isConnected[i][j] == isConnected[j][i]




# Logic
# Its a adjacency matrix DFS graph traversal problem
# Have a visited set, which will contain all the cities (nxn matrix)
# Iterate over the outer list
    # every list denotes a representation of that city
    # if not in visited call dfs
    # In dfs add it to visited
        # Run for loop on the inner list
            # Check if thats not in visited and isConneacted[start][end] == 1
                # apply dfs again





class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        provinces = 0

        def dfs(start):
            visited.add(start)
            for end in range(len(isConnected)):
                if isConneacted[start][end] and end not in visited:
                    dfs(end)

        visited = set()
        for start in range(len(isConnected)):
            if start not in visited:
                provinces += 1
                dfs(start)

        return provinces