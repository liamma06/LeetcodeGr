class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        mappings = {} 
        ans = []

        for num in nums1:
            mappings[num] = mappings.get(num,0) + 1 

        for num in nums2:
            if num in mappings and mappings[num] > 0:
                mappings[num] -= 1  # decrement so matches frequency, slowly approaches zero 
                ans.append(num)
        return ans 
                