class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        mappings = {}

        for num in nums:
            mappings[num] = mappings.get(num,0) + 1 
            if mappings[num] >= 2:
                return True

        return False 
        
        