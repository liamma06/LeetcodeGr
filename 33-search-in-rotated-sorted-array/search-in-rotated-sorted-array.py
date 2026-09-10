class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # rotation point means one side must be ascending small->big, so once we know which side is "proper"
        # - binary search that side
        # - if not on that side must be on other side 
        # - repeat from the top until target found 

        left = 0 
        right = len(nums) - 1 

        while left < right:
            mid = (left + right) // 2 

            if nums[mid] == target:
                return mid

            #is the left side properly sorted 
            if (nums[left] <= nums[mid]):
                
                #is the target actually inside the "sorted"
                if (nums[left] <= target and target <= nums[mid]):
                    right = mid-1
                else:
                    #must be the other side then 
                    left = mid + 1 
            else:
                #right side sorted, OPPOSITE of left side
                if (nums[mid] <= target and target <= nums[right]):
                    left = mid + 1
                else:
                    #must be the other side then 
                    right = mid - 1

        #senario where end of loop 
        if nums[left] == target:
            return left
        else:
            return -1
        
                

    