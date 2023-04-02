class Solution:
    def search(self, nums: List[int], target: int) -> int:
    #     return self.binary_search(nums, 0, len(nums) - 1, target)
    # def binary_search(self, nums, start, end, target):
    #         l = start
    #         r = end

    #         if l <= r:
    #             mid = (l + r) // 2
    #             if nums[mid] < target:
    #                 return self.binary_search(nums, mid + 1, r, target)
    #             elif nums[mid] > target:
    #                 return self.binary_search(nums, l, mid - 1, target)
    #             elif nums[mid] == target:
    #                 return mid
            
    #         return -1
        
        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            if nums[mid] > target:
                r = mid - 1
            elif nums[mid] < target:
                l = mid + 1
            else:
                return mid

        return -1
