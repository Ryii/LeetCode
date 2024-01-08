from typing import List
from collections import defaultdict

class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        dp = [defaultdict(int) for i in range(len(nums))]

        answer = 0

        for i in range(1, len(nums)):
            for j in range(i):
                diff = nums[i] - nums[j]
                dp[i][diff] += dp[j][diff] + 1
                answer += dp[j][diff]

        return answer