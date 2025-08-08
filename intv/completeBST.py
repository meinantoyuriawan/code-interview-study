# Definition for a binary tree node.
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class myTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, node, key):
        if node is None:
            return TreeNode(key)
        
        if node.val < key:
            node.right = self._insert(node.right, key)
        elif node.val > key:
            node.left = self._insert(node.left, key)
        return node

    def level_order(self):
        result = self._BFSTraversal(self.root)
        print(result)

    def _BFSTraversal(self, node):
        q = deque()
        res = []

        if node:
            q.append(node)
            res.append([node.val])

        while q:
            temp = []
            for i in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                    temp.append(node.left.val)
                
                if node.right:
                    q.append(node.right)
                    temp.append(node.right.val)
            res.append(temp)
        return res

    def in_order(self):
        result = self._DFSTraversal(self.root)
        print(result)

    def _DFSTraversal(self, node):
        res = []
        def dfs(node):
            if node is None:
                return
            res.append(node.val)
            dfs(node.left)
            dfs(node.right)

        dfs(node)
        return res

    def find(self, key):
        if self._find(self.root, key):
            print('found')

    def _find(self, node, key):
        if node is None:
            return False
        
        if node.val == key:
            return True
        elif node.val > key:
            return self._find(node.left, key)
        elif node.val < key:
            return self._find(node.right, key)


    def _delete(self, node, key):
        if node is None:
            return None

        if node.val < key:
            node.right = self._delete(node.right, key)
        if node.val > key:
            node.left = self._delete(node.left, key)
        if node.val == key:
            print(node.val)
            if node.left is None and node.right is None:
                return None
        
        return node
    
    def delete(self, key):
        self.root = self._delete(self.root, key)



r = myTree()
r.insert(5)
r.insert(2)
r.insert(9)
r.insert(4)
r.insert(1)

r.level_order()
r.in_order()

r.find(2)
r.find(7)

r.delete(9)
r.level_order()
r.in_order()