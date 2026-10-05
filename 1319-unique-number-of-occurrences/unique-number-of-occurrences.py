class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        freq = {}
        vals = {}

        for num in arr:
            if num in freq:
                freq[num] += 1 
            else:
                freq[num] = 1 

        for k,v in freq.items():
            if v in vals:
                return False
            else: 
                vals[v] = 1

        return True