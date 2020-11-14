# Write an algorithm to determine if a number n is "happy".
#
# A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.
#
# Return True if n is a happy number, and False if not.
#
# Example:
#
# Input: 19
# Output: true
# Explanation:
# 12 + 92 = 82
# 82 + 22 = 68
# 62 + 82 = 100
# 12 + 02 + 02 = 1


# Logic
# Here the main thing to point is that, if a number occurs twice the loop will continue
# So have a set, which contains all the int char square sum you find
# If you find it twice, it means you have found the loop
# So make sure check that
# Call the square sum function till total == 1 and n not seen in the set
# At the end if n == 1 return True else return False

class Solution:
    def isHappy(self, n: int) -> bool:
        def square_sum(num):
            total = 0
            for aint in str(num):
                total += int(aint) ** 2
            return total

        # iteration_count = 100
        seen = set()
        # while n != 1 and iteration_count > 0:
        while n != 1 and n not in seen:
            seen.add(n)
            n = square_sum(n)
            # iteration_count -= 1

        if n == 1:
            return True
        else:
            return False