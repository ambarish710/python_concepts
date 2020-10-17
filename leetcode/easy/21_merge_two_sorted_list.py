#Merge two sorted linked lists and return it as a new sorted list. The new list should be made by splicing together the nodes of the first two lists.
lx1 = [1,2,4]
lx2 = [1,3,4]

def merge_list(l1, l2):
    l3 = []
    if l1 == [] and l2 == []:
        return l3
    elif l1 and l2 == []:
        return l1
    elif l2 and l1 == []:
        return l2
    else:
        i, j = 0, 0
        while i < len(l1) and j < len(l2):
            #print(i,j)
            if l1[i] < l2[j]:
                l3.append(l1[i])
                i += 1
            else:
                l3.append(l2[j])
                j += 1

        if i == len(l1) and j != len(l2):
            l3 += l2[j:]
        elif i != len(l1) and j == len(l2):
            l3 += l1[i:]

        return l3

print(merge_list(lx1, lx2))


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        prehead = ListNode(-1)

        l3 = prehead
        if l1 == None and l2 == None:
            return l3
        elif l1 == None and l2 != None:
            return l2
        elif l1 != None and l2 == None:
            return l1
        else:
            while l1 and l2:
                if l1.val <= l2.val:
                    l3.next = l1
                    l1 = l1.next
                else:
                    l3.next = l2
                    l2 = l2.next
                l3 = l3.next
            if l1 == None and l2:
                l3.next = l2
            elif l1 and l2 == None:
                l3.next = l1

        return prehead.next