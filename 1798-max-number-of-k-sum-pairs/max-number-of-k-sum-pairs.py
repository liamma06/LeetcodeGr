class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        freq  = {}
        result = 0 

        #frequency map for O(1) search up
        for num in nums:
            if num in freq:
                freq[num] += 1 
            else:
                freq[num] = 1 

        #send look for look up 
        for num in nums:
            #make sure the current still available
            if freq[num] > 0:
                
                freq[num] -= 1 #remove for now in the case of duplicates (look == num ) make sure enough space 

                look = k - num

                #remove found matching pair. 
                if (look in freq) and freq[look] > 0 :
                    freq[look] -= 1 
                    result += 1
                else:
                    freq[num] += 1 

        return result 
        