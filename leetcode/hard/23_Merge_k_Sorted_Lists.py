# You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
#
# Merge all the linked-lists into one sorted linked-list and return it.
#
#
#
# Example 1:
#
# Input: lists = [[1,4,5],[1,3,4],[2,6]]
# Output: [1,1,2,3,4,4,5,6]
# Explanation: The linked-lists are:
# [
#   1->4->5,
#   1->3->4,
#   2->6
# ]
# merging them into one sorted list:
# 1->1->2->3->4->4->5->6
# Example 2:
#
# Input: lists = []
# Output: []
# Example 3:
#
# Input: lists = [[]]
# Output: []
#
#
# Constraints:
#
# k == lists.length
# 0 <= k <= 10^4
# 0 <= lists[i].length <= 500
# -10^4 <= lists[i][j] <= 10^4
# lists[i] is sorted in ascending order.
# The sum of lists[i].length won't exceed 10^4.


# Logic -- O(nlogn)
# Move all the elements of the list into one single list
# Sort this list
# And now create a new LL from the above sorted array list


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        # Storing all the data from the linked lists in one single python list
        self.nodes = []
        for alist in lists:
            while alist:
                self.nodes.append(alist.val)
                alist = alist.next

        # Sorting the python array/list
        self.nodes.sort()

        # Check
        if len(self.nodes) == 0:
            return

            # Assigning the first element
        head = temp = ListNode(self.nodes[0])

        for element in self.nodes[1:]:
            temp.next = ListNode(element)
            temp = temp.next

        return head