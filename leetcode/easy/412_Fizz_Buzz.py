# Write a program that outputs the string representation of numbers from 1 to n.
#
# But for multiples of three it should output “Fizz” instead of the number and for the multiples of five output “Buzz”. For numbers which are multiples of both three and five output “FizzBuzz”.
#
# Example:
#
# n = 15,
#
# Return:
# [
#     "1",
#     "2",
#     "Fizz",
#     "4",
#     "Buzz",
#     "Fizz",
#     "7",
#     "8",
#     "Fizz",
#     "Buzz",
#     "11",
#     "Fizz",
#     "13",
#     "14",
#     "FizzBuzz"
# ]



# Logic
# Observe the question problem properly
# First position there is 1, so if you use for loop need to add 1
# Check if modulo k % 3 or k % 5 or k%3 and k%5 == 0
    # Add respective strings to the list
# Else add numbers


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        ret = []

        for i in range(n):
            if ((i + 1) % 3) == 0 and ((i + 1) % 5) == 0:
                ret.append("FizzBuzz")
            elif ((i + 1) % 3) == 0:
                ret.append("Fizz")
            elif ((i + 1) % 5) == 0:
                ret.append("Buzz")
            else:
                ret.append(str(i + 1))

        return ret
