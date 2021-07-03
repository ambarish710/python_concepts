# Given a non-empty string s and an abbreviation abbr, return whether the string matches with the given abbreviation.
#
# A string such as "word" contains only the following valid abbreviations:
#
# ["word", "1ord", "w1rd", "wo1d", "wor1", "2rd", "w2d", "wo2", "1o1d", "1or1", "w1r1", "1o2", "2r1", "3d", "w3", "4"]
# Notice that only the above abbreviations are valid abbreviations of the string "word". Any other string is not a valid abbreviation of "word".
#
# Note:
# Assume s contains only lowercase letters and abbr contains only lowercase letters and digits.
#
# Example 1:
# Given s = "internationalization", abbr = "i12iz4n":
#
# Return true.
# Example 2:
# Given s = "apple", abbr = "a2e":
#
# Return false.


# Logic
# THis is medium question to be honest
# Asked in cohesity interview
# Simple and clean code



class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:

        # if there's a abbr and no word
        if abbr and not word:
            return False

        # if there's no word or abbr
        if not word and not abbr:
            return True

        i, j = 0, 0

        while i < len(word) and j < len(abbr):
            if abbr[j].isalpha():

                if word[i] != abbr[j]:
                    return False

                i += 1
                j += 1

            else:

                num = ""

                # leading zero check
                if abbr[j] == "0":
                    return False

                while j < len(abbr) and abbr[j].isdigit():
                    num += abbr[j]
                    j += 1

                i += int(num)

        if i == len(word) and j == len(abbr):
            return True
        else:
            return False