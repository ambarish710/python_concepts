# Given three integer arrays arr1, arr2 and arr3 sorted in strictly increasing order, return a sorted array of only the integers that appeared in all three arrays.
#
#
#
# Example 1:
#
# Input: arr1 = [1,2,3,4,5], arr2 = [1,2,5,7,9], arr3 = [1,3,4,5,8]
# Output: [1,5]
# Explanation: Only 1 and 5 appeared in the three arrays.
#
#
# Constraints:
#
# 1 <= arr1.length, arr2.length, arr3.length <= 1000
# 1 <= arr1[i], arr2[i], arr3[i] <= 2000


# Logic
# Keep the count of occurences in a dict counter
# Iterate over one dict counter and check if same entry exits in other two
    # If yes then append to return list
    # Else not
# Return return list


class Solution:
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        output = []

        arr1_counter = Counter(arr1)
        arr2_counter = Counter(arr2)
        arr3_counter = Counter(arr3)

        for key, value in arr1_counter.items():
            if (key in arr2_counter and arr2_counter[key] == value) and (
                    key in arr3_counter and arr3_counter[key] == value):
                output.append(key)

        return output
