# Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).
#
# For example:
# Given binary tree [3,9,20,null,null,15,7],
#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its zigzag level order traversal as:
# [
#   [3],
#   [20,9],
#   [15,7]
# ]


# Logic
# Iterate over the list using BSF (level order traversal)
# With sentinel and also keep a counter in place
    # Increment the value of the counter by 1 after each level
    # Check if counter % 2 == 0
    # If yes, insert at the last list start
    # Else append to  the last list
# Instead of having a temp list and appending it to main list
# Directly make manipulations to the original list


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from queue import Queue


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        self.ret = []

        if root == None:
            return self.ret

        def lever_order_traversal(root):
            queue = Queue()
            sentinel = "#"
            queue.put(sentinel)
            queue.put(root)
            cal = 0
            while queue.qsize() > 1:
                node = queue.get()
                if node == "#":
                    self.ret += [[]]
                    cal += 1
                    queue.put(sentinel)
                else:
                    if cal % 2 == 0:
                        self.ret[-1].insert(0, node.val)
                    else:
                        self.ret[-1].append(node.val)
                    if node.left:
                        queue.put(node.left)
                    if node.right:
                        queue.put(node.right)

        lever_order_traversal(root=root)

        print(self.ret)

        return self.ret