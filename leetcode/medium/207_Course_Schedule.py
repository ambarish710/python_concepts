# There are a total of numCourses courses you have to take, labeled from 0 to numCourses-1.
#
# Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]
#
# Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?
#
#
#
# Example 1:
#
# Input: numCourses = 2, prerequisites = [[1,0]]
# Output: true
# Explanation: There are a total of 2 courses to take.
#              To take course 1 you should have finished course 0. So it is possible.
# Example 2:
#
# Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
# Output: false
# Explanation: There are a total of 2 courses to take.
#              To take course 1 you should have finished course 0, and to take course 0 you should
#              also have finished course 1. So it is impossible.
#
#
# Constraints:
#
# The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.
# You may assume that there are no duplicate edges in the input prerequisites.
# 1 <= numCourses <= 10^5



# Logic
#...




from collections import defaultdict, deque


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # create adjacency list
        g = defaultdict(list)
        for item in prerequisites:
            g[item[1]].append(item[0])

        # create indegree dict
        # Set indegree for the number of courses to 0
        indegre = {i: 0 for i in range(numCourses)}

        for i in prerequisites:
            indegre[i[0]] += 1

        # append the 0 indegre into the queue
        q = deque()
        for k, v in indegre.items():
            if v == 0:
                q.append(k)

        cnt = 0
        while q:
            cur = q.popleft()
            cnt += 1
            if g.get(cur) != None:
                for i in g.get(cur):
                    indegre[i] -= 1
                    if indegre[i] == 0:
                        q.append(i)
        return cnt == numCourses