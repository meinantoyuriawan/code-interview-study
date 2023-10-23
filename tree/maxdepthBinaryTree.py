class TreeNode:
    def __init__(self, val=0, left=None, right=None) :
        self.val = val
        self.left = left
        self.right = right

def MaxDepth(root):
    if root:
        return 1 + max(MaxDepth(root.left), MaxDepth(root.right))
    else:
        return 0