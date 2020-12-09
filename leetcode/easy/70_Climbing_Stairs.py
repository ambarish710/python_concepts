# You are climbing a staircase. It takes n steps to reach the top.
#
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
#
#
#
# Example 1:
#
# Input: n = 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps
# Example 2:
#
# Input: n = 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step
#
#
# Constraints:
#
# 1 <= n <= 45



# Logic
# This is straightforward a dynamic programming related problem
# Consider the fibonacci sequence problem in front
# Either you can go with
    # Recursion and Memoization (Recurse and store)
    # Bottom up Approach        (Simple and efficient)
# If you try till five you will understand the mathematics behind it
    # [0, 1, 2, 3, 5, 8]
    # Next number is the sum of the last two
    # (Igoniring 1st two nums in the list, thats the same with fibonnaci nums)
# We do the same thing
    # For n == 1,2,3 have a corner case
    # For rest iterate over the for loop,
    # where next element is the sum of the last two elements
# Return that element



class Solution:
    def climbStairs(self, n: int) -> int:

        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 2

        ret = [0, 1, 2]

        for i in range(3, n + 1):
            ret.append(ret[i - 1] + ret[i - 2])

        return ret[n]
