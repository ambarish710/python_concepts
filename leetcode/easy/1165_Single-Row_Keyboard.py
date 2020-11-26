# There is a special keyboard with all keys in a single row.
#
# Given a string keyboard of length 26 indicating the layout of the keyboard (indexed from 0 to 25), initially your finger is at index 0. To type a character, you have to move your finger to the index of the desired character. The time taken to move your finger from index i to index j is |i - j|.
#
# You want to type a string word. Write a function to calculate how much time it takes to type it with one finger.
#
#
#
# Example 1:
#
# Input: keyboard = "abcdefghijklmnopqrstuvwxyz", word = "cba"
# Output: 4
# Explanation: The index moves from 0 to 2 to write 'c' then to 1 to write 'b' then to 0 again to write 'a'.
# Total time = 2 + 1 + 1 = 4.
# Example 2:
#
# Input: keyboard = "pqrstuvwxyzabcdefghijklmno", word = "leetcode"
# Output: 73
#
#
# Constraints:
#
# keyboard.length == 26
# keyboard contains each English lowercase letter exactly once in some order.
# 1 <= word.length <= 10^4
# word[i] is an English lowercase letter.


# Logic
# Initialize the last char index to 0
# Iterate over char in word
# Get current char's index
# Calculate the diff in between current and last char index
# Add that to time taken
# Return time taken

class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        time_taken = 0

        last_char_index = 0

        for char in word:
            curr_char_index = keyboard.index(char)
            diff = abs(curr_char_index - last_char_index)
            last_char_index = curr_char_index
            time_taken += diff

        return time_taken
