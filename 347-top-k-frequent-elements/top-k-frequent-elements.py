"""
Initial thoughts is creating some sort of freq mapping and sorting 
"""

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        freq = {}

        #O(n) looping through each number 
        for num in nums:
            if num not in freq: #O(1) look up 
                freq[num] = 0
            freq[num] += 1 

        #O(mlogm)
        sort_freq = sorted(freq, key=lambda k: freq[k], reverse=True)

        return sort_freq[ :k]

        #overall O(nlogn) 