# A self-dividing number is a number that is divisible by every digit it contains.
#
# For example, 128 is a self-dividing number because 128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.
#
# Also, a self-dividing number is not allowed to contain the digit zero.
#
# Given a lower and upper number bound, output a list of every possible self dividing number, including the bounds if possible.
#
# Example 1:
# Input:
# left = 1, right = 22
# Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]
# Note:
#
# The boundaries of each input argument are 1 <= left <= right <= 10000.


# Logic
# Iterate over all the nums in between left to right
    # First of all check if any char in num is 0,
        # If yes then continue else move fwd
    # Check if all chars in that string are self divisible
        # If yes add it to output list
# Return output list


class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        output = []

        for i in range(left, right + 1):
            if any(char == "0" for char in str(i)):
                continue
            if all((i % int(char)) == 0 for char in str(i)):
                output.append(i)

        return output