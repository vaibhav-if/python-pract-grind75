# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_height = 0

        def traverse_tree(node):
            nonlocal max_height
            if not node:
                return 0

            left_height = traverse_tree(node.left)
            right_height = traverse_tree(node.right)

            max_height = max(max_height, left_height + right_height)

            return 1 + max(left_height, right_height)

        traverse_tree(root)
        return max_height
    

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
s = Solution()
print(s.diameterOfBinaryTree(root))