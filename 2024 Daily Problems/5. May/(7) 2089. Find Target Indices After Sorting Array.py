class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        ans = []
        for i, n in enumerate(nums):
            if n == target:
                ans.append(i)
        return ans