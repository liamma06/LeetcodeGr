class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        max_ones = 0
        zeros = 0
        left = 0

        k = 1

        for right in range(len(nums)):
            if nums[right] == 0:
                zeros += 1 

            while zeros > k: 
                if nums[left] == 0: 
                    zeros -= 1 
                
                left += 1

            #no including hte zero(since not flipped)
            max_ones = max(right - left, max_ones)

        return max_ones #O(n) different approach keeping track of zeros instead of 1's
