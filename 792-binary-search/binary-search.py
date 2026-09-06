class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #L & R indxs 
        left = 0 
        right = len(nums) - 1 

        while left <= right:
            #index
            mid = (left + right) // 2 

            if nums[mid] == target:
                return mid 
            #since it less it should be on the right side (shift over right)
            elif nums[mid] < target: 
                left = mid+ 1 
            #greater then shift over to the left 
            elif nums[mid] > target:
                right = mid -1
            #- / + bc we alreayd checked mid 

        return -1