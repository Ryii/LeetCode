from typing import List
from collections import bisect_left
from functools import lru_cache

class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = sorted(list(zip(startTime, endTime, profit)))
        startTime = [jobs[i][0] for i in range(len(startTime))]

        @lru_cache(None)
        def dp(i):
            if i == len(startTime): 
                return 0
            
            ans = dp(i + 1)

            j = bisect_left(startTime, jobs[i][1])
            ans = max(ans, dp(j) + jobs[i][2])
            return ans

        return dp(0)