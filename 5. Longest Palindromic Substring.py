class Solution:
    def longestPalindrome(self, s: str) -> str:
        length = 0
        longest = ""
        
        for i in range(0, len(s)):
            l = i
            r = i
            
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > length:
                    longest = s[l:r+1]
                    length = r - l + 1
                l -= 1
                r += 1
            
            l = i
            r = i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > length:
                    longest = s[l:r+1]
                    length = r - l + 1
                l -= 1
                r += 1
                
        return longest