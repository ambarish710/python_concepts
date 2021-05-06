# A pangram is a sentence where every letter of the English alphabet appears at least once.
#
# Given a string sentence containing only lowercase English letters, return true if sentence is a pangram, or false otherwise.
#
#
#
# Example 1:
#
# Input: sentence = "thequickbrownfoxjumpsoverthelazydog"
# Output: true
# Explanation: sentence contains at least one of every letter of the English alphabet.
# Example 2:
#
# Input: sentence = "leetcode"
# Output: false
#
#
# Constraints:
#
# 1 <= sentence.length <= 1000
# sentence consists of lowercase English letters.


# Logic
# Create a list with all chars (all_chars)
# Count the occurences of each element (char count dict)
# Iterate over the dict and remove the char from all_chars list
# If after iteration len(all_chars) == 0
    # Then return True else return False

import string

class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        all_chars = list(string.ascii_lowercase)
        char_count = Counter(sentence)

        for char in char_count.keys():
            all_chars.remove(char)

        if len(all_chars) == 0:
            return True

        return False
