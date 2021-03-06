# 572. Subtree of Another Tree
# Easy
#
# 2714
#
# 125
#
# Add to List
#
# Share
# Given two non-empty binary trees s and t, check whether tree t has exactly the same structure and node values with a subtree of s. A subtree of s is a tree consists of a node in s and all of this node's descendants. The tree s could also be considered as a subtree of itself.
#
# Example 1:
# Given tree s:
#
#      3
#     / \
#    4   5
#   / \
#  1   2
# Given tree t:
#    4
#   / \
#  1   2
# Return true, because t has the same structure and node values with a subtree of s.
#
#
# Example 2:
# Given tree s:
#
#      3
#     / \
#    4   5
#   / \
#  1   2
#     /
#    0
# Given tree t:
#    4
#   / \
#  1   2
# Return false.
#


# Logic
# The logic pretty intuitive but hard to explain
# Read twice (asked very less times)


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        # if node in s matches head node of t, then check if isSame
        def dfs(s):
            if not s or not t: return False
            if s.val == t.val:
                if isSame(s, t): return True

            return dfs(s.left) or dfs(s.right)

        # checks if two trees are the same
        def isSame(s, t):
            if not t and not s: return True
            if (not s or not t) or (s.val != t.val):
                return False

            return isSame(s.left, t.left) and isSame(s.right, t.right)

        return dfs(s)