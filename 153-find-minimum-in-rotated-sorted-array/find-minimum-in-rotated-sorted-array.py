class Solution:
    def findMin(self, nums: List[int]) -> int:
        #if rotated there should be a spot where the left > right in a sorted array 
        #aka mid > right there shoudl be a rotational point inside 

        #indexes
        left = 0    
        right = len(nums) - 1

        while left < right:
            mid = (left + right) // 2 

            
            if (nums[mid] > nums[right]):
                # mid is on the "high" side before the rotation point, so the minimum must be to the right of mid
                #shift over from mid since can't be 
                left = mid + 1

            elif (nums[mid] < nums[right]):
                # mid is already past the rotation point (or IS the minimum), so keep mid in the search space and shrink from the right
                right = mid 

        return nums[left]



