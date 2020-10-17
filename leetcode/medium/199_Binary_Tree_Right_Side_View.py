# Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.
#
# Example:
#
# Input: [1,2,3,null,5,null,4]
# Output: [1, 3, 4]
# Explanation:
#
#    1            <---
#  /   \
# 2     3         <---
#  \     \
#   5     4       <---

from queue import Queue


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if root is None:
            return []

        self.queue = Queue()
        self.result = []
        self.queue.put(root)

        while not self.queue.empty():
            self.current_level = []
            for i in range(0, self.queue.qsize()):
                node = self.queue.get()
                self.current_level.append(node.val)

                if node.left:
                    self.queue.put(node.left)
                if node.right:
                    self.queue.put(node.right)

            self.result.append(self.current_level[-1])

        return self.result