# Definition for a binary tree node.

import collections
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



class Solution:
    def levelOrder(self, root):
        res = []

        q = collections.deque()
        q.append(root)

        # add the root into queue, first queue will be an element of 1 node

        while q:
            # measure the length of queue
            # init a level list
            qLen = len(q)
            level = []
            for i in range(qLen):
                # iterate through range of queue, pop the root element
                node = q.popleft()
                # if node is not null
                if node:
                    # append the node value to level list
                    # append the left and right children nodes into queue, now the length will be 2.
                    # the queue will going on and if it is reaching null (no child) then it will stopped
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            # for every iteration, if there is element in level, append it to res
            if level:
                res.append(level)

        return res