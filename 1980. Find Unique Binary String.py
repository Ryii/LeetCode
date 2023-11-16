from typing import List

class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        answer = ""

        for i in range(len(nums)):
            answer += '1' if nums[i][i] == '0' else '0'

        return answer