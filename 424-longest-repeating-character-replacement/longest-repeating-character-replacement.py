class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0 
        maxCount = 0 
        seen = {} # wahtinside window
        longest = 0

        for right in range(len(s)):
            char = s[right]

            #there is match 
            if char in seen:
                seen[char] += 1
            else:
                seen[char] = 1

            maxCount = max(seen.values())

            if (right-left + 1 ) - maxCount > k: # this is waht is there versus not and checking if within that of k 
                seen[s[left]] -= 1 # left leaves so need to remvoe that in the current scope 
                left +=1 

            longest = max(longest, right -left + 1 )
            
        

        return longest

        