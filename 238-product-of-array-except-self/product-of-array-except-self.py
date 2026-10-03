class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        """
            Intial thought to have some sort of collective product and divide out using division for the current value However we cna't do that 
        """
        left = [] 
        right = [0]* len(nums)

        for i in range(len(nums)):
            if i == 0:
                left.append(1)
            else:
                val = left[i - 1] * nums[i - 1]
                left.append(val)     

        for i in range(len(nums) - 1 , -1, -1 ):
            if i == len(nums) - 1 :
                right[i] = 1
            else:
                right[i] = right[i + 1 ] * nums[ i +1]


        result = [0] * len(nums)
        for i in range(len(nums)):
            result[i] = left[i] * right[i]

        return result

        #O(3N) still O(n) possibly recompute on same run like left could have result already inside as left right and multiple directly in
