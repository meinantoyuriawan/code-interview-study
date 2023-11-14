class TreeNode:
    def __init__(self, val=0, left=None, right=None) :
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSame(self, p, q):

        # if p or q:
        #     self.isSame(p.left, q.left)
        #     self.isSame(p.right, q.right)
        # else:
        #     return False
        
        # return True

        # empty tree, corner case for every child that is same
        if not p and not q:
            return True
        # tree not empty and root.value p and q is same
        if p and q and p.val == q.val:
            # recursive calls for each root between left and right
            # and logic, if one of the conditions unmet then return false
            return self.isSame(p.left, q.left) and self.isSame(p.right, q.right)
        else:
            return False