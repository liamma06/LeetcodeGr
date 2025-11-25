class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        max_ones = 0
        left = 0
        curr = 0
        num_of_zeros= 0
        zero = False

        for i in range(len(nums)):
            if nums[i] == 1:
                curr+=1
            elif nums[i] == 0:
                num_of_zeros += 1
                zero = True
            while num_of_zeros > 1:
                if nums[left] == 0:
                    num_of_zeros -= 1
                elif nums[left] == 1:
                    curr -= 1
                left+=1
            max_ones = max(curr,max_ones)

            if zero == False:
                max_ones -= 1

        return max_ones
                
                