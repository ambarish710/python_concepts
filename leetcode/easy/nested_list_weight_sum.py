# Given a nested list of integers, return the sum of all integers in the list weighted by their depth.
#
# Each element is either an integer, or a list -- whose elements may also be integers or other lists.
#
# Example 1:
# Input: [[1,1],2,[1,1]]
# Output: 10
# Explanation: Four 1's at depth 2, one 2 at depth 1.
#
# Example 2:
# Input: [1,[4,[6]]]
# Output: 27
# Explanation: One 1 at depth 1, one 4 at depth 2, and one 6 at depth 3; 1 + 4*2 + 6*3 = 27.

class Solution:
    def depthSum(self, nestedList, depth, total=0):
        for element in nestedList:
            if type(element) == list:
                depth += 1
                total += self.depthSum(element, depth)
                depth -= 1
            else:
                total += element * depth
        return total

if __name__ == "__main__":
    #nestedList = [[1, 1], 2, [1, 1]]
    nestedList = [1,[4,[6]]]
    s_obj = Solution()
    total = s_obj.depthSum(nestedList=nestedList, depth=1)
    print("Total -- {}".format(total))
