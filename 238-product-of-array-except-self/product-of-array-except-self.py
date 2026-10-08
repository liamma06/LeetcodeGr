class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        """
            initial thoughts is kina just loop through everything besides the current every single value which would be really slow and take a lot of time 

            Need a way to almost track everything all togther 
            -have a left side -> tracking product until that point 
            -have a right side- > do the same but other side  
        """

        """
            nums = [1,2,3,4]

            left = [1,1,2,6]
            right = [24,12,4,1]
            result = [24,12,8,6]
            
            i = 0 

        """
        length = len(nums)

        left = [0] * length
        right = [0] * length
        result = [0] * length

        #O(n) 
        for i in range(length):
            if i == 0:
                left[i] = 1
                continue
            left[i] = left[i - 1] * nums[i - 1]

        #O(n)
        #range(start, stop, step)
        for i in range(length - 1, -1 ,-1):
            if i == length - 1:
                right[i] = 1
                continue
            right[i] = right[ i + 1] * nums[i + 1]

        #O(n)
        for i in range(length):
            result[i] = left[i] * right[i] 

        return result 

        #overall is O(3n) which is still O(n) 

