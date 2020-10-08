# Design a data structure that supports adding new words and finding if a string matches any previously added string.
#
# Implement the WordDictionary class:
#
# WordDictionary() Initializes the object.
# void addWord(word) Adds word to the data structure, it can be matched later.
# bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise. word may contain dots '.' where dots can be matched with any letter.
#
# Example:
#
# Input
# ["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
# [[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
# Output
# [null,null,null,null,false,true,true,true]
#
# Explanation
# WordDictionary wordDictionary = new WordDictionary();
# wordDictionary.addWord("bad");
# wordDictionary.addWord("dad");
# wordDictionary.addWord("mad");
# wordDictionary.search("pad"); // return False
# wordDictionary.search("bad"); // return True
# wordDictionary.search(".ad"); // return True
# wordDictionary.search("b.."); // return True
#
# Constraints:
#
# 1 <= word.length <= 500
# word in addWord consists lower-case English letters.
# word in search consist of  '.' or lower-case English letters.
# At most 50000 calls will be made to addWord and search.

# TRIE DATA STRUCTURE

def __init__(self):
    """
    Initialize your data structure here.
    """
    self.trie = {}


def addWord(self, word: str) -> None:
    """
    Adds a word into the data structure.
    """
    node = self.trie
    for character in word:
        if character not in node:
            node[character] = {}
        node = node[character]
    node["$"] = True


def search(self, word: str) -> bool:
    """
    Returns if the word is in the data structure. A word could contain the dot character '.' to represent any letter.
    """

    def search_in_node(word, node) -> bool:
        for i, ch in enumerate(word):
            if not ch in node:

                # if the current character is '.'
                # check all possible nodes at this level
                if ch == '.':
                    for x in node:
                        if x != '$' and search_in_node(word[i + 1:], node[x]):
                            return True

                # if no nodes lead to answer
                # or the current character != '.'
                return False

            # if the character is found
            # go down to the next level in trie
            else:
                node = node[ch]

        return '$' in node

    return search_in_node(word, self.trie)
