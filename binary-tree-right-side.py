from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> list[int]:
        if not root:
            return []
        
        tree_queue = [[root, 0]] # [node, level]
        rightview = []
        last_level = 0
        rightmost = 0
        while(tree_queue):
            node, level = tree_queue.pop(0)
            if node.left:
                tree_queue.append([node.left, level+1])
            if node.right:
                tree_queue.append([node.right, level+1])

            if level == last_level:
                rightmost = node.val
            else:
                rightview.append(rightmost)
                last_level = level
                rightmost = node.val

        rightview.append(rightmost)
        return rightview


sol = Solution()
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.right = TreeNode(5)
root.right.right = TreeNode(4)
print(sol.rightSideView(root))