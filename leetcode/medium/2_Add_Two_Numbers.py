# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
#
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
#
#
#
# Example 1:
#
#
# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.
# Example 2:
#
# Input: l1 = [0], l2 = [0]
# Output: [0]
# Example 3:
#
# Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Output: [8,9,9,9,0,0,0,1]
#
#
# Constraints:
#
# The number of nodes in each linked list is in the range [1, 100].
# 0 <= Node.val <= 9
# It is guaranteed that the list represents a number that does not have leading zeros.


# Logic
# Iterate over linked list 1 and form num1 (reverse it)
# Iterate over linked list 2 and form num2 (reverse it)
# Add num1 + num2 and store it in a different variable num3 (reverse it)
# Create new LL by iterating over num3


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # Number 1
        num1 = ""
        while l1:
            num1 += str(l1.val)
            l1 = l1.next
        num1 = num1[::-1]

        # Number 2
        num2 = ""
        while l2:
            num2 += str(l2.val)
            l2 = l2.next
        num2 = num2[::-1]

        # Adding Numbers
        num3 = str(int(num1) + int(num2))[::-1]

        # Converting it to list
        if num3:
            self.head = ListNode(val=num3[0])
            temp_ptr = self.head
            for char in num3[1:]:
                temp_ptr.next = ListNode(val=char)
                temp_ptr = temp_ptr.next
        else:
            return None

        return self.head