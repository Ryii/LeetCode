from typing import List

class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        arr.sort()
        dp = {}
        
        for i in arr:
            dp[i] = 1
            
        for index, root in enumerate(arr):
            for leaf1 in arr[0: index]:
                if root % leaf1 == 0:
                    leaf2 = root // leaf1
                    
                    if leaf2 in arr:
                        dp[root] += dp[leaf1] * dp[leaf2]
                    
        return sum(dp.values()) % (10**9 + 7)