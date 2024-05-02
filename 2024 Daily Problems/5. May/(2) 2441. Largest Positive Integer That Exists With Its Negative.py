class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        hmap = set(nums)
        largest = -1
        for n in nums:
            if -n in hmap:
                largest = max(largest, n, -n) 

        return largest