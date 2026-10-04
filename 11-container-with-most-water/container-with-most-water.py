class Solution:
    def maxArea(self, height: list[int]) -> int:
        #have one on the left  and right to keep track

        left = 0 
        right = len(height) - 1 
        max_output = 0 

        while left < right:
            
            #calcualte output 
            output = min(height[left], height[right]) * (right - left)
            
            max_output = max(output, max_output)

            #shift the lower one over
            if height[right] >= height[left]:
                left += 1
            elif height[left] >= height[right]:
                right -= 1 

        return max_output

        #O(n)