class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        map1 = [0] * 26
        map2 = [0] * 26
        
        for i in word1:
            map1[ord(i) - ord('a')] += 1
        for c in word2:
            map2[ord(c) - ord('a')] += 1
            
        for i in range(26):
            if map1[i] == 0 and map2[i] != 0 or map1[i] == 0 and map2[i] != 0:
                return False
            
        return sorted(map1) == sorted(map2)