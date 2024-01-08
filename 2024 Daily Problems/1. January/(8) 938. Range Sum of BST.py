from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        total = 0
        
        def helper(root):
            nonlocal total
            if not root:
                return
            if root.val >= low and root.val <= high:
                total += root.val
                helper(root.left)
                helper(root.right)
            elif root.val < low:
                helper(root.right)
            else:
                helper(root.left)
            
        helper(root)
            
        return total