from typing import List

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        dp = [[0] * n for i in range(n)]
        
        if n == 1:
            return matrix[0][0]
        
        for i in range(n):
            dp[0][i] = matrix[0][i]
            
        for r in range(1, n):
            for c in range(n):
                if c == 0:
                    dp[r][c] = min(dp[r-1][c], dp[r-1][c+1]) + matrix[r][c]
                elif c == n - 1:
                    dp[r][c] = min(dp[r-1][c-1], dp[r-1][c]) + matrix[r][c]
                else:
                    dp[r][c] = min(dp[r-1][c-1], dp[r-1][c], dp[r-1][c+1]) + matrix[r][c]
        
        return min(dp[-1])
                