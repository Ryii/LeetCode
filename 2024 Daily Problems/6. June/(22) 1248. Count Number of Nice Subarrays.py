class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        curr_sum = 0
        subarrays = 0
        hmap = {curr_sum: 1}

        for i in range(len(nums)):
            curr_sum += nums[i] % 2
            if curr_sum - k in hmap:
                subarrays += hmap[curr_sum - k]
            hmap[curr_sum] = hmap.get(curr_sum, 0) + 1

        print(hmap)
        return subarrays