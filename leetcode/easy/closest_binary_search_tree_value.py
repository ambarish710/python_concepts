# Given a non-empty binary search tree and a target value, find the value in the BST that is closest to the target.
#
# Note:
#
# Given target value is a floating point.
# You are guaranteed to have only one unique value in the BST that is closest to the target.
# Example:
#
# Input: root = [4,2,5,1,3], target = 3.714286
#
#     4
#    / \
#   2   5
#  / \
# 1   3
#
# Output: 4

# BST Travesal with additional checks
from queue import Queue


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:

        if root == None:
            return None

        closest = root.val
        difference = abs(target - root.val)
        self.queue = Queue()
        self.queue.put(root)

        while not self.queue.empty():
            node = self.queue.get()
            if node.val != None:
                if abs(node.val - target) < difference:
                    closest = node.val
                    difference = abs(node.val - target)

            if node.left:
                self.queue.put(node.left)

            if node.right:
                self.queue.put(node.right)

        return closest
