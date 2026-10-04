class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        max_ones = 0
        curr_ones = 0 
        flipped = 0 

        left = 0 

        for right in range(len(nums)):
            if nums[right] == 1:
                curr_ones += 1 
            elif nums[right] == 0:
                flipped += 1 
                curr_ones += 1 
            
            while flipped > k:
                curr_ones -= 1 

                if nums[left] == 0 :
                    flipped -= 1

                left += 1 
            
            max_ones = max(curr_ones, max_ones)

        return max_ones

            

        
        