# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid(node, left, right):
            if not node:
                return True
            print(f"node {node.val} left {left} right {right}")
            
            if not (node.val > left and node.val < right):
                return False
            

            return (valid(node.left, left, node.val) and valid(node.right, node.val, right))
        
        return valid(root, float("-inf"), float("inf"))

t = TreeNode(5)
t.left = TreeNode(3)
t.right = TreeNode(7)
t.left.left = None
t.left.right = None
t.right.left = TreeNode(4)
t.right.right = TreeNode(8)

sol = Solution()
print(sol.isValidBST(t))