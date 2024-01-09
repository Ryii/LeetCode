from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        list1 = []
        list2 = []
        
        def helper(root, List):
            if root is None:
                return
            if root.left is None and root.right is None:
                List.append(root.val)
                return
            else:
                helper(root.left, List)
                helper(root.right, List)
        
        helper(root1, list1)
        helper(root2, list2)
        
        return list1 == list2