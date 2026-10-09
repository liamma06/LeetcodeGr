class Solution:
    def maxArea(self, height: list[int]) -> int:
        """
            reading this it seems like you need to track the start and the end and shift whichever one is less in hope to find a new max?
        """
        left = 0 
        right = len(height) - 1 
        max_water = float('-inf')

        #O(n) 
        while left < right:
            lower = min(height[left], height[right])
            area = lower * (right - left)

            max_water = max(area, max_water)

            if height[right] == lower:
                right -= 1 
            else:
                left += 1 

        return max_water