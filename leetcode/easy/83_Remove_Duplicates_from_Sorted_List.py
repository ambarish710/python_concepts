# Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.
#
#
#
# Example 1:
#
#
# Input: head = [1,1,2]
# Output: [1,2]
# Example 2:
#
#
# Input: head = [1,1,2,3,3]
# Output: [1,2,3]
#
#
# Constraints:
#
# The number of nodes in the list is in the range [0, 300].
# -100 <= Node.val <= 100
# The list is guaranteed to be sorted in ascending order.



# Logic
# Corner Cases check
    # If LL empty
    # If LL contains just one element
# Initializing prev and curr ptrs
# Iterating over LL and removing duplicates
# Return head


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        # Corner Cases check
        # If LL empty
        if head == None:
            return None

        # If LL contains just one element
        if head.next == None:
            return head

        # Initializing prev and curr ptrs
        prev = head
        curr = prev.next

        # Iterating over LL and removing duplicates
        while curr:
            if curr.val == prev.val:
                prev.next = curr.next
            else:
                prev = curr
            curr = curr.next

        # Return head
        return head