from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = 1
        post = 1
        answer = [1] * len(nums)

        length = len(nums)

        for i in range(length):
            answer[i] = pre
            pre *= nums[i]

        for i in range(length - 1, -1, -1):
            answer[i] *= post
            post *= nums[i]

        return answer
        