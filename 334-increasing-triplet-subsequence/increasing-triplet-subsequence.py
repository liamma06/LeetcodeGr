class Solution:
    def increasingTriplet(self, nums: list[int]) -> bool:
        """
            iterate thourgh have an array track the left min 
            right max at that point
        """
        right_max_track= [0] * len(nums)
        
        #purpose is to see if the max at that point
        for i in range(len(nums)-1 , -1, -1):
            if i == len(nums) - 1: 
                right_max = nums[i]
            else:
                right_max = max(nums[i], right_max)

            right_max_track[i] = right_max
        
        left_min_track = [0] *len(nums)

        for i in range(0,len(nums) -1, 1):
            if i == 0:
                left_min = nums[i]
            else:
                left_min= min(nums[i],left_min)
            left_min_track[i] = left_min
            
            if i >= 1 and left_min_track[i -1] < nums[i] < right_max_track[i+1]:
                return True

        return False
            
                

            
        

        
        