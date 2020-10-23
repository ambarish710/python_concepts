# 127. Word Ladder
# Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation sequence from beginWord to endWord, such that:
#
# Only one letter can be changed at a time.
# Each transformed word must exist in the word list.
# Note:
#
# Return 0 if there is no such transformation sequence.
# All words have the same length.
# All words contain only lowercase alphabetic characters.
# You may assume no duplicates in the word list.
# You may assume beginWord and endWord are non-empty and are not the same.
# Example 1:
#
# Input:
# beginWord = "hit",
# endWord = "cog",
# wordList = ["hot","dot","dog","lot","log","cog"]
#
# Output: 5
#
# Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
# return its length 5.
# Example 2:
#
# Input:
# beginWord = "hit"
# endWord = "cog"
# wordList = ["hot","dot","dog","lot","log"]
#
# Output: 0
#
# Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.

# Logic -- Time Complexity O(n^3)
# If endword not in wordlist return 0
# Apply BFS, starting with putting beginWord into the queue
# Convert string to array as strings are immutable
# Try exchanging each char of the word in queue with all letters in alphabet
# Till either you find the end word then return level +1
# Elif if you find word in wordlist add the letter to queue
# Increment level after each for loop iteration and make sure to replace orginal char back again once word checks done





from queue import Queue
import string


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # Corner Case
        if endWord not in wordList:
            return 0

        self.queue = Queue()
        self.queue.put(beginWord)
        self.level = 1
        self.all_alphabets = string.ascii_lowercase[0:26]

        while not self.queue.empty():
            qsize = self.queue.qsize()
            for i in range(0, qsize):
                word_array = list(self.queue.get())
                for i, original_char in enumerate(word_array):
                    for char in self.all_alphabets:
                        if char == original_char:
                            continue
                        word_array[i] = char
                        new_word = ''.join(word_array)

                        if new_word == endWord:
                            return self.level + 1

                        if new_word in wordList:
                            self.queue.put(new_word)
                            #wordList.remove(new_word)

                    word_array[i] = original_char

            self.level += 1

        return 0
