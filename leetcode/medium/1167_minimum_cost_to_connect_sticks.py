# 1167. Minimum Cost to Connect Sticks
# Medium
# You have some number of sticks with positive integer lengths. These lengths are given as an array sticks, where sticks[i] is the length of the ith stick.
#
# You can connect any two sticks of lengths x and y into one stick by paying a cost of x + y. You must connect all the sticks until there is only one stick remaining.
#
# Return the minimum cost of connecting all the given sticks into one stick in this way.
#
#
#
# Example 1:
#
# Input: sticks = [2,4,3]
# Output: 14
# Explanation: You start with sticks = [2,4,3].
# 1. Combine sticks 2 and 3 for a cost of 2 + 3 = 5. Now you have sticks = [5,4].
# 2. Combine sticks 5 and 4 for a cost of 5 + 4 = 9. Now you have sticks = [9].
# There is only one stick left, so you are done. The total cost is 5 + 9 = 14.
# Example 2:
#
# Input: sticks = [1,8,3,5]
# Output: 30
# Explanation: You start with sticks = [1,8,3,5].
# 1. Combine sticks 1 and 3 for a cost of 1 + 3 = 4. Now you have sticks = [4,8,5].
# 2. Combine sticks 4 and 5 for a cost of 4 + 5 = 9. Now you have sticks = [9,8].
# 3. Combine sticks 9 and 8 for a cost of 9 + 8 = 17. Now you have sticks = [17].
# There is only one stick left, so you are done. The total cost is 4 + 9 + 17 = 30.
# Example 3:
#
# Input: sticks = [5]
# Output: 0
# Explanation: There is only one stick, so you don't need to do anything. The total cost is 0.
#
#
# Constraints:
#
# 1 <= sticks.length <= 104
# 1 <= sticks[i] <= 104


# Logic
# The logic here is to add the smallest sticks together and their sum to list
# And do the process again till one stick is remaining
# OR
# Use min heap -- Its a special DS where Min Heap (get smallest element from the list each time when pop)
# All the elements in the heap are unsorted, when ever you do a push or pop, order is mantained
# (next time you pop you'll get the smallest element)

import bisect


class Solution(object):
    def connectSticks(self, sticks):
        """
        :type sticks: List[int]
        :rtype: int
        """
        if len(sticks) <= 1:
            return 0

        # Sorting the sticks in descending order
        sticks.sort(reverse=True)

        # Returning minimum cost of connecting all sticks into one stick
        total = 0
        while len(sticks) > 1:
            s1, s2 = sticks.pop(), sticks.pop()
            s3 = s1 + s2
            total += s3

            # Approach 1
            sticks.append(s3)
            sticks.sort(reverse=True)

            # Approach 2 -- Time Limit Exceeded
            # for i in range(0, len(sticks)):
            #     if s3 <= sticks[i]:
            #         sticks.insert(i, s3)
            #         break

            # Approach 3 -- Time Limit Exceeded
            # bisect.insort(sticks, s3)

        return total

# OR

import heapq

class Solution(object):
    def connectSticks(self, sticks):
        """
        :type sticks: List[int]
        :rtype: int
        """
        heapq.heapify(sticks)
        res = 0
        while len(sticks)>1:
            p1 = heapq.heappop(sticks)
            p2 = heapq.heappop(sticks)
            res+=p1+p2
            heapq.heappush(sticks,p1+p2)
        return res