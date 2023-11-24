from typing import List

class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        indexM, indexP, indexG = 0, 0, 0
        total = 0
        
        for i in range(len(garbage) - 1, -1, -1):
            stop = garbage[i]
            total += len(stop)
            if indexM == 0 and 'M' in stop: indexM = i
            if indexP == 0 and 'P' in stop: indexP = i
            if indexG == 0 and 'G' in stop: indexG = i

        total += sum(travel[:indexM]) + sum(travel[:indexP]) + sum(travel[:indexG])
        return total