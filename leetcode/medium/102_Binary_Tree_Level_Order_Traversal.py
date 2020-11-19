# Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).
#
# For example:
# Given binary tree [3,9,20,null,null,15,7],
#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its level order traversal as:
# [
#   [3],
#   [9,20],
#   [15,7]
# ]


# Logic
# Perform level order traversal with sentinel logic
# Add the sentinel and traverse (BFS)
# Have a main list which you will return in future
# Have a queue, add to the queue
# Take data from queue and add it to temp list
# Check if queue get is sentinel, if yes then add temp list to main list and re-initialize temp_list to []
# if queue.left exists add it to the queue similarly for queue.right



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


from queue import Queue

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:

        # Corner Cases
        if root == None:
            return []
        if root.left == None and root.right == None:
            return [[root.val]]

        self.queue = Queue()
        self.sentinel = "#"
        self.queue.put(self.sentinel)
        self.queue.put(root)
        self.lot_output = []
        self.level = []

        while self.queue.qsize() > 1:
            node = self.queue.get()
            if node == "#":
                if self.level != []:
                    self.lot_output.append(self.level)
                    self.level = []
                self.queue.put(self.sentinel)
            else:
                self.level.append(node.val)
                if node.left:
                    self.queue.put(node.left)
                if node.right:
                    self.queue.put(node.right)

        self.lot_output.append(self.level)
        return self.lot_output