from typing import List

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        
        total = 0
        
        for cookie in s:
            if cookie >= g[0]:
                total += 1
                g.pop(0)
                if not g:
                    return total
                
        return total