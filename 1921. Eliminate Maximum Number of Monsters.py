import math
from typing import List

class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        turnsTilTouch = sorted([math.ceil(d / s) for d, s in zip(dist, speed)])
        
        for i, t in enumerate(turnsTilTouch, 1):
            if i > t:
                return t
        
        return len(dist)