from typing import List

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        hmap = {}
        
        for n in arr:
            hmap[n] = hmap.get(n, 0) + 1
            
        return len(hmap) == len(set(hmap.values()))