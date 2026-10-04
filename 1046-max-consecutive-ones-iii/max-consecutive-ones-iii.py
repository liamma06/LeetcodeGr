class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        max_ones = 0
        curr_ones = 0 
        flipped = 0 

        left = 0 

        for right in range(len(nums)):

            #incrmenet curr_ones including the flipped zeros too
            if nums[right] == 1:
                curr_ones += 1 
            elif nums[right] == 0:
                flipped += 1 
                curr_ones += 1 
            
            #if we used all the flipped we just move left until we have a free one again
            while flipped > k:
                curr_ones -= 1 

                if nums[left] == 0 :
                    flipped -= 1

                left += 1 
            
            max_ones = max(curr_ones, max_ones)

        return max_ones #O(n) still tho 

        """
        class Solution:
            def longestOnes(self, nums: list[int], k: int) -> int:
                max_ones = 0
                zeros = 0
                left = 0

                for right in range(len(nums)):
                    if nums[right] == 0:
                        zeros += 1

                    while zeros > k:
                        if nums[left] == 0:
                            zeros -= 1
                        left += 1

                    max_ones = max(max_ones, right - left + 1)

                return max_ones
        """

            

        
        