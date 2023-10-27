from collections import defaultdict
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = defaultdict(list)

        for i, n in enumerate(nums):
            if target - n in hashMap:
                return [hashMap[target - n], i]
            else:
                hashMap.update({n : i})