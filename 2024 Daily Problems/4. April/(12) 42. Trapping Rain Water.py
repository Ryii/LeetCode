class Solution:
    def trap(self, height: List[int]) -> int:
        total = 0
        left, right = 0, (len(height)-1)
        left_max, right_max = height[left], height[right]

        while left < right:
            if left_max < right_max:
                if height[left+1] < left_max:
                    total += left_max - height[left+1]
                left_max = max(left_max, height[left+1])
                left += 1
                print("left", left, total)
            else:
                if height[right-1] < right_max:
                    total += right_max - height[right-1]
                right_max = max(right_max, height[right-1])
                right -= 1
                print("right", right, total)

        return total