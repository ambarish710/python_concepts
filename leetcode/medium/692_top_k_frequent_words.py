# 692. Top K Frequent Words
# Given a non-empty list of words, return the k most frequent elements.
#
# Your answer should be sorted by frequency from highest to lowest. If two words have the same frequency, then the word with the lower alphabetical order comes first.
#
# Example 1:
# Input: ["i", "love", "leetcode", "i", "love", "coding"], k = 2
# Output: ["i", "love"]
# Explanation: "i" and "love" are the two most frequent words.
#     Note that "i" comes before "love" due to a lower alphabetical order.
# Example 2:
# Input: ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], k = 4
# Output: ["the", "is", "sunny", "day"]
# Explanation: "the", "is", "sunny" and "day" are the four most frequent words,
#     with the number of occurrence being 4, 3, 2 and 1 respectively.
# Note:
# You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
# Input words contain only lowercase letters.
# Follow up:
# Try to solve it in O(n log k) time and O(n) extra space.


# Logic
# Iterate over words list and count the word frequency and put it in dict
# where key is the word (string) and value is its frequency (int)
# Sort the dict by values in descending order and key in ascending order (using sorted method)
# Return k elements from the sorted list (sorted method to sort dict converts it into a list)

from collections import defaultdict

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        self.output = []

        if k <= 0:
            return self.output

        self.word_count = defaultdict(int)

        for word in words:
            self.word_count[word] += 1

        def my_sort_func(x):
            return -x[1], x[0]

        self.sorted_word_count = sorted(self.word_count.items(), key=my_sort_func)

        if k >= len(self.sorted_word_count):
            return [word[0] for word in self.sorted_word_count]
        else:
            for i in range(0, k):
                self.output.append(self.sorted_word_count[i][0])
            return self.output
