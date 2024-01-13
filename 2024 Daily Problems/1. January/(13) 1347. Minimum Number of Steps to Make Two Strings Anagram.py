class Solution:
    def minSteps(self, s: str, t: str) -> int:
        sMap = [0] * 26
        tMap = [0] * 26
        
        for c in s:
            sMap[ord(c)-ord('a')] += 1
        for c in t:
            tMap[ord(c)-ord('a')] += 1
            
        total = 0
        for i in range(26):
            total += abs(sMap[i] - tMap[i])
            
        return total // 2