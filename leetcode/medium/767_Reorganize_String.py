# Given a string S, check if the letters can be rearranged so that two characters that are adjacent to each other are not the same.
#
# If possible, output any possible result.  If not possible, return the empty string.
#
# Example 1:
#
# Input: S = "aab"
# Output: "aba"
# Example 2:
#
# Input: S = "aaab"
# Output: ""
# Note:
#
# S will consist of lowercase letters and have length in range [1, 500].


#Logic
# Create a list with empty strings with size of S
# COunt the number of chars and put them in a dict
# Sort this dict in reverse order
# Check if the first element is greater than len(S)/2
    # return ""
# Else
    # Iterate over the sorted word count dict
    # Start filling words at alternate positions in newly created list
# Return the string made from the list


from collections import Counter
import math


class Solution:
    def reorganizeString(self, S: str) -> str:
        s_length = len(S)

        count_dict = Counter(S)

        def mysort_func(x):
            return x[1]

        sorted_count_dict = sorted(count_dict.items(),
                                   key=mysort_func,
                                   reverse=True)

        lst = [""] * s_length

        if sorted_count_dict[0][1] > math.ceil(s_length / 2):
            return ""
        else:
            # Insert character in not-adjacent positions
            idx = 0
            for k, v in sorted_count_dict:
                left_v = v
                while idx < s_length and left_v > 0:
                    lst[idx] = k
                    idx += 2
                    left_v -= 1

                # return to the front and continue to insert
                if idx >= s_length and left_v > 0:
                    idx = 1
                    while idx < s_length and left_v > 0:
                        lst[idx] = k
                        idx += 2
                        left_v -= 1

            return "".join(lst)