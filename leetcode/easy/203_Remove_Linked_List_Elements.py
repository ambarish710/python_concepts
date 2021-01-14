# Remove all elements from a linked list of integers that have value val.
#
# Example:
#
# Input:  1->2->6->3->4->5->6, val = 6
# Output: 1->2->3->4->5




# Logic
# Making sure first element is not val, if yes replace it
# Corner Cases
# Checking if LL is empty
# Checking if LL contains just one element
# Assigning prev and curr ptrs
# Check# Assigning prev and curr ptrsing if LL contains just one element
# Returning head




# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        # Making sure first element is not val, if yes replace it
        while head and head.val == val:
            head = head.next

        # Corner Cases
        # Checking if LL is empty
        if head == None:
            return

        # Checking if LL contains just one element
        if head.next == None:
            if head.val == val:
                return None
            else:
                return head

        # Assigning prev and curr ptrs
        prev = head
        curr = prev.next

        # Iterating over the LL and deleting required elements
        while curr:
            if curr.val == val:
                prev.next = curr.next
            else:
                prev = curr
            curr = curr.next

        # Returning head
        return head