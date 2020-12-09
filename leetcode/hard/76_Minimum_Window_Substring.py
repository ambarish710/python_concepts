# Given two strings s and t, return the minimum window in s which will contain all the characters in t. If there is no such window in s that covers all characters in t, return the empty string "".
#
# Note that If there is such a window, it is guaranteed that there will always be only one unique minimum window in s.
#
#
#
# Example 1:
#
# Input: s = "ADOBECODEBANC", t = "ABC"
# Output: "BANC"
# Example 2:
#
# Input: s = "a", t = "a"
# Output: "a"
#
#
# Constraints:
#
# 1 <= s.length, t.length <= 105
# s and t consist of English letters.
#
#
# Follow up: Could you find an algorithm that runs in O(n) time?


# LOGIC
# Approach 1 -- My Solution O(n^4) not a good solution
# Brute Force -- Iterate over all possible substrings and keep a Counter of all the temp substrings
# Make sure all the elements and their counts are present in the tempstring (more is fine)
# If a sub string falls under that category, add it to the set
# Return the lowest element in the set


# Approach 2
# Sliding Window
# We start with two pointers, leftleft and rightright initially pointing to the first element of the string SS.
# We use the right pointer to expand the window until we get a desirable window i.e. a window that contains all of the characters of TT.
# Once we have a window with all the characters, we can move the left pointer ahead one by one. If the window is still a desirable one we keep on updating the minimum window size.
# If the window is not desirable any more, we repeat step \; 2step2 onwards.


from collections import Counter
import time

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Corner Case
        if len(s) < len(t):
            return ""

        # Array to add all the sub-strings
        self.substrings = []
        t_counter = Counter(t)

        for i in range(0, len(s)):
            for j in range(i, len(s)):
                temp_string = s[i:j + 1]
                temp_string_counter = Counter(temp_string)
                if all(temp_string_counter[char_count] >= t_counter[char_count] for char_count in
                       t_counter) and temp_string not in self.substrings:
                    self.substrings.append(temp_string)

        # all(container[x] >= contained[x] for x in contained)
        # Check
        if len(self.substrings) == 0:
            return ""

        # Sort Function
        def my_sort_func(x):
            return len(x)

        # Sort
        self.substrings.sort(key=my_sort_func)

        return self.substrings[0]




    def minWindow(self, s: str, t: str) -> str:
        need, missing = Counter(t), len(t)
        i, WindowStart, WindowEnd = 0, 0, 0
        for j, char in enumerate(s, 1):
            if need[char] > 0:
                missing -= 1
            need[char] -= 1

            # condition to shrink window
            if not missing:
                while i < j and need[s[i]] < 0:
                    need[s[i]] += 1
                    i += 1
                if not WindowEnd or j-i <= WindowEnd-WindowStart:
                    WindowStart, WindowEnd = i, j
            j += 1
        return s[WindowStart:WindowEnd]

if __name__ == "__main__":
    s_obj = Solution()
    #output = s_obj.minWindow(s="ADOBECODEBANC",t="ABC")
    s = "wegdtzwabazduwwdysdetrrctotpcepalxdewzezbfewbabbseinxbqqplitpxtcwwhuyntbtzxwzyaufihclztckdwccpeyonumbpnuonsnnsjscrvpsqsftohvfnvtbphcgxyumqjzltspmphefzjypsvugqqjhzlnylhkdqmolggxvneaopadivzqnpzurmhpxqcaiqruwztroxtcnvhxqgndyozpcigzykbiaucyvwrjvknifufxducbkbsmlanllpunlyohwfsssiazeixhebipfcdqdrcqiwftutcrbxjthlulvttcvdtaiwqlnsdvqkrngvghupcbcwnaqiclnvnvtfihylcqwvderjllannflchdklqxidvbjdijrnbpkftbqgpttcagghkqucpcgmfrqqajdbynitrbzgwukyaqhmibpzfxmkoeaqnftnvegohfudbgbbyiqglhhqevcszdkokdbhjjvqqrvrxyvvgldtuljygmsircydhalrlgjeyfvxdstmfyhzjrxsfpcytabdcmwqvhuvmpssingpmnpvgmpletjzunewbamwiirwymqizwxlmojsbaehupiocnmenbcxjwujimthjtvvhenkettylcoppdveeycpuybekulvpgqzmgjrbdrmficwlxarxegrejvrejmvrfuenexojqdqyfmjeoacvjvzsrqycfuvmozzuypfpsvnzjxeazgvibubunzyuvugmvhguyojrlysvxwxxesfioiebidxdzfpumyon"
    t = "ozgzyywxvtublcl"
    t1 = time.time()
    output = s_obj.minWindow(s=s, t=t)
    t2 = time.time()
    print(output)
    print("Time Taken: {}".format(t2-t1))
