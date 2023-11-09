class Solution:
    def countHomogenous(self, s: str) -> int:
        total = 0
        cur = 0
        prev = ''
        for n in s:
            if n != prev:
                cur = 1
                prev = n
            else:
                cur += 1
            total += cur
        
        return total % (10**9 + 7)