from typing import List

class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        maxSum = 0

        for i in range(len(nums)//2):
            maxSum = max(nums[i] + nums[len(nums)-1-i], maxSum)

        return maxSum