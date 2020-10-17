# 763. Partition Labels
# Medium
#
# 3417
#
# 140
#
# Add to List
#
# Share
# A string S of lowercase English letters is given. We want to partition this string into as many parts as possible so that each letter appears in at most one part, and return a list of integers representing the size of these parts.
#
#
#
# Example 1:
#
# Input: S = "ababcbacadefegdehijhklij"
# Output: [9,7,8]
# Explanation:
# The partition is "ababcbaca", "defegde", "hijhklij".
# This is a partition so that each letter appears in at most one part.
# A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits S into less parts.
#
#
# Note:
#
# S will have length in range [1, 500].
# S will consist of lowercase English letters ('a' to 'z') only.


# Logic
# For all characters, note the start and the end position {char: [start, end]} and update it in a dict called index_position
# Now traverse this index_position dict (in a for loop)
# For example consider the first char's start1 and end1 position1
# Add all the next occurring characters till start is less than end1
# Make sure to update end1, if start is less than end1
# This gives you the start and end indexes, take the len of the this string and add it to return list
# Eval--> TC - O(log n)



from collections import defaultdict

class Solution:
    def partitionLabels(self, S):
        s_len = len(S)

        if s_len == 0 :
            return []
        if s_len == 1:
            return [1]

        output_list = []
        index_position = defaultdict(list)

        for i, char in enumerate(S):
            if char not in index_position:
                index_position[char] = [i, i]
            else:
                index_position[char][1] = i

        temp_list = []
        for entity, value in index_position.items():
            #print(temp_list)
            if temp_list == []:
                temp_list += index_position[entity]
            else:
                if value[0] < temp_list[1]:
                    if value[1] > temp_list[1]:
                        temp_list[1] = value[1]
                else:
                    output_list.append(len(S[temp_list[0]:temp_list[1]+1]))
                    temp_list = index_position[entity]

        output_list.append(len(S[temp_list[0]:temp_list[1] +1]))
        #print(index_position)
        #print(output_list)
        return output_list


if __name__ == "__main__":
    s_obj = Solution()
    s_obj.partitionLabels(S = "ababcbacadefegdehijhklij")
