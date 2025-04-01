class Solution:
    def maxArea(self, height: list[int]) -> int:
        max_area = 0
        left = 0
        right = len(height) - 1
        while left < right:
            if height[left] <= height[right]:
                area = height[left] * (right - left)
                left += 1
            else:
                area = height[right] * (right - left)
                right -= 1
            
            if area > max_area:
                max_area = area
        
        return max_area

sol = Solution()
print(sol.maxArea([1,8,6,2,5,4,8,3,7]))