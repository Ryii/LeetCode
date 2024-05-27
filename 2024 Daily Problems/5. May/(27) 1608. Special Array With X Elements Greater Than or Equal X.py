class Solution:
    def specialArray(self, nums: List[int]) -> int:
        freq = [0] * (len(nums) + 1)
        for n in nums:
            freq[min(len(nums), n)] += 1
        curSum = 0
        for i in range(len(nums), -1, -1):
            curSum += freq[i]
            if curSum == i:
                return i
        return -1