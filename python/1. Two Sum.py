from collections import defaultdict

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hashMap = defaultdict(list)

        for i, n in enumerate(nums):
            if target - n in hashMap:
                return [hashMap[target - n], i]
            else:
                hashMap.update({n : i})