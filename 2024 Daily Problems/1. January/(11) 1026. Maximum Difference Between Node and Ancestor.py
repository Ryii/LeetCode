from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        maxdiff = 0
        
        def helper(root, max_val, min_val):
            nonlocal maxdiff
            if not root:
                maxdiff = max(maxdiff, max_val - min_val)
                return
            newmax = max(max_val, root.val)
            newmin = min(min_val, root.val)
            helper(root.left, newmax, newmin)
            helper(root.right, newmax, newmin)
        
        helper(root, 0, 100000)
        
        return maxdiff