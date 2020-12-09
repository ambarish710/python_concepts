# Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.
#
# k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.
#
# Follow up:
#
# Could you solve the problem in O(1) extra memory space?
# You may not alter the values in the list's nodes, only nodes itself may be changed.
#
#
# Example 1:
#
#
# Input: head = [1,2,3,4,5], k = 2
# Output: [2,1,4,3,5]
# Example 2:
#
#
# Input: head = [1,2,3,4,5], k = 3
# Output: [3,2,1,4,5]
# Example 3:
#
# Input: head = [1,2,3,4,5], k = 1
# Output: [1,2,3,4,5]
# Example 4:
#
# Input: head = [1], k = 1
# Output: [1]
#
#
# Constraints:
#
# The number of nodes in the list is in the range sz.
# 1 <= sz <= 5000
# 0 <= Node.val <= 1000
# 1 <= k <= sz


# Logic
# Algorithm
# Assuming we have a reverse() function already defined for a linked list.
# This function would take the head of the linked list and also an integer value representing k.
#
# We don't have to reverse till the end of the linked list.
# Only k nodes are to be touched at a time.
#
# In every recursive call, we first count the number of nodes in the linked list.
# As soon as the count reaches k, we break.
#
# If there are less than k nodes left in the list, we return the head of the list.
# However, if there are at least k nodes in the list, then we reverse these nodes by calling our reverse() function defined in the first step.
#
# Our recursion function needs to return the head of the reversed linked list.
# This would simply be the kth nodes in the list passed to the recursion function because after reversing the first k nodes, the k^thkth node will become the new head and so on.
# So, in every recursive call, we first reverse k nodes, then recurse on the rest of the linked list.
# When recursion returns, we establish the proper connections.


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseLinkedList(self, head, k):

        # Reverse k nodes of the given linked list.
        # This function assumes that the list contains
        # atleast k nodes.
        new_head, ptr = None, head
        while k:
            # Keep track of the next node to process in the
            # original list
            next_node = ptr.next

            # Insert the node pointed to by "ptr"
            # at the beginning of the reversed list
            ptr.next = new_head
            new_head = ptr

            # Move on to the next node
            ptr = next_node

            # Decrement the count of nodes to be reversed by 1
            k -= 1

        # Return the head of the reversed list
        return new_head

    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:

        count = 0
        ptr = head

        # First, see if there are atleast k nodes
        # left in the linked list.
        while count < k and ptr:
            ptr = ptr.next
            count += 1

        # If we have k nodes, then we reverse them
        if count == k:
            # Reverse the first k nodes of the list and
            # get the reversed list's head.
            reversedHead = self.reverseLinkedList(head, k)

            # Now recurse on the remaining linked list. Since
            # our recursion returns the head of the overall processed
            # list, we use that and the "original" head of the "k" nodes
            # to re-wire the connections.
            head.next = self.reverseKGroup(ptr, k)
            return reversedHead
        return head


from collections import Counter
name = "Gaurav Sood Ambarish Pandharikar Vick Balaji #@$@$%^^(* nsdkjfhasdkjfanosudbfaknsdbfkabsdkhfbaksd fjhabsdnf ajshdb fna sdjhgfasdbghkabskdjg"
count_dictionary = Counter(name)
count_dictionary.most_common()