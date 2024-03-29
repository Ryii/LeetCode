# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional
from collections import deque
from typing import List

class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        ans = []
        curVals = []
        
        q = deque()
        q.append(root)
        
        while q:
            level_len = len(q)
            curMax = float('-inf')
            for i in range(level_len):
                node = q.popleft()
                curMax = max(curMax, node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                
            ans.append(curMax)
        
        return ans