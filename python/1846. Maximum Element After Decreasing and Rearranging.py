from typing import List

class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()
        maxLen = 1

        for i in range(1, len(arr)):
            if arr[i] > maxLen:
                maxLen += 1

        return maxLen