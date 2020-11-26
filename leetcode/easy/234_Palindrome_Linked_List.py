# Given a singly linked list, determine if it is a palindrome.
#
# Example 1:
#
# Input: 1->2
# Output: false
# Example 2:
#
# Input: 1->2->2->1
# Output: true
# Follow up:
# Could you do it in O(n) time and O(1) space?


# Logic
# Approach 1
# simple approach add data to a list
# And check is reverse of the list equal to the current list
# Return true if it is, else not

# Approach 2
# Recursion
# Self explanatory read it


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    # Approach 1
    def isPalindrome(self, head: ListNode) -> bool:
        ints = []
        while head:
            ints.append(head.val)
            head = head.next

        if ints == ints[::-1]:
            return True
        else:
            return False


    # Approach 2
    def isPalindrome(self, head: ListNode) -> bool:
        self.front_pointer = head

        def recursively_check(current_node=head):
            if current_node is not None:
                if not recursively_check(current_node.next):
                    return False
                if self.front_pointer.val != current_node.val:
                    return False
                self.front_pointer = self.front_pointer.next
            return True

        return recursively_check()


