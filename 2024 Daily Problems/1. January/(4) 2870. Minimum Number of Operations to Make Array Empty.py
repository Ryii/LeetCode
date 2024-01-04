from typing import List

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        hmap = {}
        
        for n in nums:
            hmap[n] = hmap.get(n, 0) + 1
            
        total = 0
            
        for num, count in hmap.items():
            if count <= 1:
                return -1
            
            quo, rem = count // 3, count % 3
            total += quo
            total += 1 if rem else 0
            
        return total