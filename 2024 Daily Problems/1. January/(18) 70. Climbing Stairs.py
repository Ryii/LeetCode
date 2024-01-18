class Solution:
    def climbStairs(self, n: int) -> int:
        step1, step2 = 1, 2
        
        for i in range(3, n+1):
            steps = step1 + step2
            step1 = step2
            step2 = steps
            
        return step2 if n != 1 else step1

#         s1, s2 = 1, 1

#         for i in range(n - 1):
#             temp = s1
#             s1 = s2
#             s2 = temp + s2

#         return s2