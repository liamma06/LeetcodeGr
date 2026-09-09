class Solution:
    def findMin(self, nums: List[int]) -> int:
        #if rotated there should be a spot where the left > right in a sorted array 
        #aka mid > right there shoudl be a rotational point inside 

        #indexes
        left = 0    
        right = len(nums) - 1

        while left < right:
            mid = (left + right) // 2 

            #rotation points within
            if (nums[mid] > nums[right]):
                #can't be mid need rotation point 
                left = mid + 1
            #not within but could be mid still  
            elif (nums[mid] < nums[right]):
                #keep mid since it could 
                right = mid 

        return nums[left]



