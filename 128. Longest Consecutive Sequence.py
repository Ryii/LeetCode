class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        hashSet = set(nums)
        sol = 0

        for n in nums:
            if (n - 1) not in hashSet:
                length = 0
                while n + length in hashSet:
                    length += 1
                sol = max(sol, length)

        return sol