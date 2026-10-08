class Solution:
    def increasingTriplet(self, nums: list[int]) -> bool:
        """
            iniially when I read this quesiton I thought tou just pick the value and scan outwards but that would be super slow contstant check for each 

            just need a way just to know some point within the right is greater and same goes for the left side. Some point is less. 

            This could mean just tracking the least/max at each point 
        """
        length = len(nums)

        left = [0] * length
        right = [0] * length 

        #O(n)
        for i in range(length):
            if i == 0:
                left[i] = nums[i]
                continue

            left[i] = min (left[i-1], nums[i-1])

        #O(n)
        #start, stop, change 
        for i in range(length-1,-1,-1):
            if i == length - 1:
                right[i] = nums[i]
                continue 
            right[i] = max(right[i+1], nums[i+1])

        #O(n)
        for i in range(length):
            if left[i] < nums[i] < right[i]:
                return True

        return False

        #overall O(n) 

            
                

            
        

        
        