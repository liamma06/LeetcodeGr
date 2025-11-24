class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        #keep track of how many ones currently while adding to number even if 0 as long the number of flipped is below the allowed amount. If it is above or equal need to reduce all on the left side until the number of flipped reduces. 

        #it always increments it is just a matter of realizing when it is useing more than the allowed flips when you would reduce. 

        max_ones = 0
        curr = 0
        use_k = 0 
        left = 0

        for i in range(len(nums)):
            curr += 1 
            if nums[i] == 0:
                use_k +=1 
            while use_k > k:
                if nums[left] == 0:
                   use_k -= 1
                curr -= 1 
                left += 1
                    
            max_ones = max(curr,max_ones)

        return max_ones



            
