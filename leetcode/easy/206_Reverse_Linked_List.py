# Reverse a singly linked list.
#
# Example:
#
# Input: 1->2->3->4->5->NULL
# Output: 5->4->3->2->1->NULL
# Follow up:
#
# A linked list can be reversed either iteratively or recursively. Could you implement both?


# Logic -- Recursion
# Recursively call the function which does the reverse mapping

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        self.head = head

        def rev_ll(current, previous):
            """
                USING RECURSION
            """
            if current == None:
                self.head = previous
                return

            rev_ll(current=current.next, previous=current)
            current.next = previous

        def reversing_the_linked_list(current, previous):
            if self.head == None or self.head.next == None:
                return
            else:
                rev_ll(current, previous)

        reversing_the_linked_list(current=self.head, previous=None)

        return self.head

    str1 = "123"
    str1.is