class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        mapping = {}

        #mapping out the frequencies 
        for num in nums:
            mapping[num] = mapping.get(num,0) + 1 

        ans = 0 

        for key,freq in mapping.items():
            if freq >= 2:
                return key 