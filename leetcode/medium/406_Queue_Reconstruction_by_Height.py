# Suppose you have a random list of people standing in a queue. A pair of integers [hi, ki] describe each person, where hi is the height of the ith person and ki is the number of people in front of the ith person who has a height greater than or equal to hi. Write an algorithm to reconstruct the queue.
#
#
#
# Example 1:
#
# Input: people = [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]
# Output: [[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]]
# Example 2:
#
# Input: people = [[6,0],[5,0],[4,0],[3,2],[2,2],[1,4]]
# Output: [[4,0],[5,0],[2,2],[3,2],[1,4],[6,0]]
#
#
# Constraints:
#
# 1 <= people.length <= 2000
# 0 <= hi <= 106
# 0 <= ki < people.length
# It is guaranteed that the input is valid.


# Logic
# Sort people by height in descending order and then using position
# Then iterate over this sorted list
# And add folks to their respective position using inset


class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        def my_sort_func(x):
            return -x[0], x[1]

        people.sort(key=my_sort_func)

        output = []

        for p in people:
            output.insert(p[1], p)

        return output

