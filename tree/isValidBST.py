# Definition for a binary tree node.
import collections
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    # def isValidBST(self, root):
    #     # bfs
    #     q = collections.deque()
    #     q.append(root)

    #     while q:
    #         node = q.popleft()
 
    #         if node:
    #             if node.left.val < node.val and node.right.val > node.val:
    #                 q.append(node.left)
    #                 q.append(node.right)
    #             else:
    #                 return False
                
    #     return True
    
    # dfs
    def isValidBST(self, root):

        def valid(node, left, right):
            if not node:
                return True
            
            if not(left < node.val < right):
                return False

            return(valid(node.left, left, node.val) and valid(node.right, node.val, right))
        return valid(root, float("-inf"), float("inf"))
    

    # bfs
    # def isValidBST(self, root: Optional[TreeNode]) -> bool:
    #     q=deque()
    #     q.append((root,-sys.maxsize,sys.maxsize))
    #     while q:
    #         currentNode,leftRange,rightRange=q.popleft()
    #         if currentNode:
    #             if not(leftRange<currentNode.val<rightRange):
    #                 return False
    #             q.append((currentNode.left,leftRange,currentNode.val))
    #             q.append((currentNode.right,currentNode.val,rightRange))
    #     return True
