# International Morse Code defines a standard encoding where each letter is mapped to a series of dots and dashes, as follows: "a" maps to ".-", "b" maps to "-...", "c" maps to "-.-.", and so on.
#
# For convenience, the full table for the 26 letters of the English alphabet is given below:
#
# [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
# Now, given a list of words, each word can be written as a concatenation of the Morse code of each letter. For example, "cab" can be written as "-.-..--...", (which is the concatenation "-.-." + ".-" + "-..."). We'll call such a concatenation, the transformation of a word.
#
# Return the number of different transformations among all words we have.
#
# Example:
# Input: words = ["gin", "zen", "gig", "msg"]
# Output: 2
# Explanation:
# The transformation of each word is:
# "gin" -> "--...-."
# "zen" -> "--...-."
# "gig" -> "--...--."
# "msg" -> "--...--."
#
# There are 2 different transformations, "--...-." and "--...--.".
# Note:
#
# The length of words will be at most 100.
# Each words[i] will have length in range [1, 12].
# words[i] will only consist of lowercase letters.


# Logic
# Have a morse code list
# Iterate over words in word_list
    # Iterate over char in word
    # Convert it to given morse code word, referring from the list
    # Add the entire representation of word to morse code conversion in a set
# Return the set




class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse_code = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.",
                      "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]

        unique_word = set()

        for word in words:
            code_word = ""
            for char in word:
                # print(ord(char) - ord("a"))
                code_word += morse_code[ord(char) - ord("a")]
            unique_word.add(code_word)

        return len(unique_word)