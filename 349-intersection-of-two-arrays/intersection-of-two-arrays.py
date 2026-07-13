class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        mappings = {}
        result = [] 

        #fill out frequency table 
        for num in nums1:
            mappings[num] = mappings.get(num,0) + 1 

        #go through and check if it matches 
        for num in nums2:
            if num in mappings and mappings[num] > 0 :
                mappings[num]  = 0  #make zero so doesn't repeat 
                result.append(num) 

        return result

