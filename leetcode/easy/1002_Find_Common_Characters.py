# Given an array A of strings made only from lowercase letters, return a list of all characters that show up in all strings within the list (including duplicates).  For example, if a character occurs 3 times in all strings but not 4 times, you need to include that character three times in the final answer.
#
# You may return the answer in any order.
#
#
#
# Example 1:
#
# Input: ["bella","label","roller"]
# Output: ["e","l","l"]
# Example 2:
#
# Input: ["cool","lock","cook"]
# Output: ["c","o"]
#
#
# Note:
#
# 1 <= A.length <= 100
# 1 <= A[i].length <= 100
# A[i][j] is a lowercase letter


# Logic
# Create a common chars list
# Sort the input list by length of the each string size
# Take the samlest string, get counter of it call it as def_char_count
# Get counter of rest all the strings from the sorted list and store it in new list
# Now iterate over elements in def_char_count
    # And check if key exists in all counter lists
    # And get the min common value
    # update the common chars list
# return common chars list



from collections import Counter


class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        common_chars = []

        # Sorting on the basis of length
        #         def myfunc(x):
        #             return len(x)

        #         A.sort(key=myfunc)

        def_word = A[0]
        def_char_count = Counter(def_word)
        print(def_char_count)

        all_word_char_count = [Counter(word) for word in A[1:]]
        print(all_word_char_count)

        for key, value in def_char_count.items():
            temp_count = float("inf")
            for word_char in all_word_char_count:
                if key in word_char:
                    temp_count = min(temp_count, word_char[key], value)
                else:
                    break
            else:
                common_chars += [key] * temp_count

        return common_chars
