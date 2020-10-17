# 249. Group Shifted Strings
# Medium
#
# Given a string, we can "shift" each of its letter to its successive letter, for example: "abc" -> "bcd". We can keep "shifting" which forms the sequence:
#
# "abc" -> "bcd" -> ... -> "xyz"
# Given a list of non-empty strings which contains only lowercase alphabets, group all strings that belong to the same shifting sequence.
#
# Example:
#
# Input: ["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"],
# Output:
# [
#   ["abc","bcd","xyz"],
#   ["az","ba"],
#   ["acef"],
#   ["a","z"]
# ]


# Logic
# You can use tuple as the key to the dict
# Take any string into consideration, form a tuple after subtraction the first characters ord
# with all the characters with % 26
# It will be same for all the shifted strings
# Store them in defaultdict where unique tuple is the key
# Return lists

# ["abc"] --> ["bcd"]
#   012         123
#Subs 0         1
#   012         012
#   %26         %26
#   14          14


from collections import defaultdict

class Solution:
    def groupStrings(self, strings):

        def hashfunc(self, string):
            return tuple( [ ( ord(c) - ord(string[0]) ) % 26 for c in string])

        self.groups = defaultdict(list)
        for string in strings:
            self.groups[hashfunc(self, string)].append(string)
        print(self.groups)
        return self.groups.values()

if __name__ == "__main__":
    s_obj = Solution()
    input_values = ["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"]
    print(s_obj.groupStrings(strings=input_values))
