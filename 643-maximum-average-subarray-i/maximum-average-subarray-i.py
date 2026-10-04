class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        left = 0
        max_avg = float('-inf') 
        window_sum = 0

        for right in range(len(nums)):
            window_sum += nums[right]

            #zero index
            if (right - left + 1) == k:

                #compute avg & store it 
                avg = window_sum / k 
                max_avg = max( avg, max_avg)

                #iterate 
                window_sum -= nums[left]
                left += 1  
        return max_avg 

            
            
