class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxArea = 0
        bigger= 0
        length = 0
        L=0

        R = len(height)-1 
        while L < R:
            bigger = min(height[L],height[R])
            length = R-L
            maxArea = max(maxArea,(bigger*length))
            if height[L] < height[R]:
                L += 1
            else:
                R -= 1
            
        return maxArea