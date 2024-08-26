"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    
    def helper(self, root, output):
        if not root:
            return
        
        for child in root.children:
            self.helper(child, output)
        
        output.append(root.val)
        return

    def postorder(self, root: 'Node') -> List[int]:
        output = []
        self.helper(root, output)

        return output
    
