class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count0 = 0
        count1 = 0
        
        for n in nums:
            if n == 0:
                count0 += 1
            elif n == 1:
                count1 += 1
                
        nums[:count0] = [0] * count0
        nums[count0:count0+count1] = [1] * count1
        nums[count0+count1:] = [2] * (len(nums) - count0 - count1)
        
        return nums