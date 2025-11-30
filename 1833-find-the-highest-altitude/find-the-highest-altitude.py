class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        highest = 0
        curr = 0
        for i in range(len(gain)):
            curr += gain[i]
            highest = max(highest,curr)

        return highest