# Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.
#
#
#
# Example 1:
#
# Input: s = "Let's take LeetCode contest"
# Output: "s'teL ekat edoCteeL tsetnoc"
# Example 2:
#
# Input: s = "God Ding"
# Output: "doG gniD"
#
#
# Constraints:
#
# 1 <= s.length <= 5 * 104
# s contains printable ASCII characters.
# s does not contain any leading or trailing spaces.
# There is at least one word in s.
# All the words in s are separated by a single space.


# Logic
# Split the string
# Iterate over the splitted string
# reverse each word and add space
# return reversed string

class Solution:
    def reverseWords(self, s: str) -> str:
        reversed_string = ""

        splitted_string = s.split(" ")

        for string in splitted_string:
            reversed_string += " " + string[::-1]

        return reversed_string.strip()