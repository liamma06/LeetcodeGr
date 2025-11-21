class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        """
        maxAvg = float('-inf')  
        num_of_shifts = len(nums) - k +1
        

        #do a sub array of k and shift one each until it reaches the end 
        
        for i in range(num_of_shifts):
            sumavg = 0 
            for j in range(k):
                sumavg += nums[j+i]
            maxAvg = max(maxAvg,sumavg/k)
        
        return maxAvg
        """

        nums_of_shifts = len(nums) - k + 1

        sub_sum = 0

        for i in range(k):
            sub_sum += nums[i]
        maxAvg = sub_sum/k

        for i in range(1,nums_of_shifts):
            sub_sum -= nums[i - 1]
            sub_sum += nums[i+k-1]
            maxAvg = max(maxAvg, sub_sum/k)
        return maxAvg

            

        
            