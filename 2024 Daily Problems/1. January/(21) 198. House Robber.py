from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])
        
        house1, house2 = nums[0], max(nums[0], nums[1])
        
        for i in range(2, n):
            temp = max(house2, nums[i] + house1)
            house1 = house2
            house2 = temp
            
        return house2
