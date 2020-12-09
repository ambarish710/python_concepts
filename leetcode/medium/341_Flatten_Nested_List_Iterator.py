# Given a nested list of integers, implement an iterator to flatten it.
#
# Each element is either an integer, or a list -- whose elements may also be integers or other lists.
#
# Example 1:
#
# Input: [[1,1],2,[1,1]]
# Output: [1,1,2,1,1]
# Explanation: By calling next repeatedly until hasNext returns false,
#              the order of elements returned by next should be: [1,1,2,1,1].
# Example 2:
#
# Input: [1,[4,[6]]]
# Output: [1,4,6]
# Explanation: By calling next repeatedly until hasNext returns false,
#              the order of elements returned by next should be: [1,4,6].



# Logic
# Create a python list by iterating over the nested list using the given funcs
# Have a ptr which initializes to -1
# Once you have the list ready
# Update the next method
    # Increment the ptr and return the value at the position of ptr in the list
# As part of hasNext
    # Check if ptr + 1 is less than the list created
    # If yes then return True else False


class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.nested = []
        self.ptr = -1

        def iterate(alist):
            for item in alist:
                if item.isInteger():
                    self.nested.append(item.getInteger())
                else:
                    iterate(alist=item.getList())

        iterate(alist=nestedList)

    def next(self) -> int:
        self.ptr += 1
        return self.nested[self.ptr]

    def hasNext(self) -> bool:
        if self.ptr + 1 < len(self.nested):
            return True
        else:
            return False
