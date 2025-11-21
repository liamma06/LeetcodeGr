class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        #sort num array so easily can test biggest with smallest!if too big move right inward, too small move left

        L = 0 
        R = len(nums)-1 
        output = 0

        if len(nums) ==0:
            return output

        new_nums = sorted(nums)

        while L < R:
            if new_nums[L] + new_nums[R] == k:
                output += 1 
                #forogt to increment inward after right
                L+=1 
                R-=1
            elif  new_nums[L]+new_nums[R] > k:
                R-=1
            elif new_nums[L]+new_nums[R] < k:
                L += 1
        return output  
