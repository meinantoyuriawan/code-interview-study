# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root, p, q):

        while True:
            if p.val < root.val and q.val < root.val:
                # self.lowestCommonAncestor(root.left, p, q)
                root = root.left
            elif p.val > root.val and q.val > root.val:
                # self.lowestCommonAncestor(root.right, p, q)
                root = root.right
            else :
                return root

