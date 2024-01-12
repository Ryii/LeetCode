class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        
        n = len(s) // 2
        first, second = s[:n], s[n:]
        
        count1, count2 = 0, 0
        
        for c in first:
            count1 += 1 if c in vowels else 0
            
        for c in second:
            count2 += 1 if c in vowels else 0
        
        return count1 == count2