# Given a list of the scores of different students, items, where items[i] = [IDi, scorei] represents one score from a student with IDi, calculate each student's top five average.
#
# Return the answer as an array of pairs result, where result[j] = [IDj, topFiveAveragej] represents the student with IDj and their top five average. Sort result by IDj in increasing order.
#
# A student's top five average is calculated by taking the sum of their top five scores and dividing it by 5 using integer division.
#
#
#
# Example 1:
#
# Input: items = [[1,91],[1,92],[2,93],[2,97],[1,60],[2,77],[1,65],[1,87],[1,100],[2,100],[2,76]]
# Output: [[1,87],[2,88]]
# Explanation:
# The student with ID = 1 got scores 91, 92, 60, 65, 87, and 100. Their top five average is (100 + 92 + 91 + 87 + 65) / 5 = 87.
# The student with ID = 2 got scores 93, 97, 77, 100, and 76. Their top five average is (100 + 97 + 93 + 77 + 76) / 5 = 88.6, but with integer division their average converts to 88.
# Example 2:
#
# Input: items = [[1,100],[7,100],[1,100],[7,100],[1,100],[7,100],[1,100],[7,100],[1,100],[7,100]]
# Output: [[1,100],[7,100]]
#
#
# Constraints:
#
# 1 <= items.length <= 1000
# items[i].length == 2
# 1 <= IDi <= 1000
# 0 <= scorei <= 100
# For each IDi, there will be at least five scores.




# Logic
# Create a high_five_dict which is a default dict list
    # Where key is the ID and list contains all the scores for that ID
# Iterate over the high_five_dict of list
    # Sort the list in reverse order for each ID
    # Take the first five elements and calculate the average
# Store it in a list (id, avg) in a new list
    # For some weird reason they want the id's to be sorted as well
# So sort the newly created list on the basis of ID's
# And return it



from collections import defaultdict


class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        output = []
        high_five_dict = defaultdict(list)

        for uid, score in items:
            high_five_dict[uid].append(score)

        for key, value in high_five_dict.items():
            value.sort(reverse=True)
            hf_avg = int(sum(value[:5]) / len(value[:5]))
            output.append([key, hf_avg])

        def my_sort_func(x):
            return x[0]

        output.sort(key=my_sort_func)

        return output