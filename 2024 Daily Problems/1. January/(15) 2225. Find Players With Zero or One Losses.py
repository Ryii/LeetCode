from typing import List

class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        hmap = {}
        # player: loss count
        
        for match in matches:
            win, lose = match[0], match[1]
            
            if win not in hmap:
                hmap[win] = 0

            hmap[lose] = hmap.get(lose, 0) + 1
            
        first, second = [], []
        
        for key, item in hmap.items():
            if item == 0:
                first.append(key)
            if item == 1:
                second.append(key)
                
        return [sorted(first), sorted(second)]