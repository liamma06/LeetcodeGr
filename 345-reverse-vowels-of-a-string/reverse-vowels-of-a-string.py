class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = "AEIOUaeiou"
        storage = [] 

        for char in s:
            if char in vowels:
                storage.append(char)
        
        #can't directly change string in place 
        result = []
        for i in range(len(s)):
            if s[i] in vowels:
                result.append(storage.pop())
            else:
                result.append(s[i])
        
        return "".join(result)

        #O(2n) so O(N)

        """
            left = 0 
            right = len(s) - 1 
            vowels = "AEIOUaeiou"
            chars = list(s)

            while left < right: 
                
                #keep going until left reachs a vowel 
                while left < right and chars[left] not in vowels:
                    left += 1 
                
                #keep going until right reaches a vowel 
                while left < right and chars[right] not in vowels:
                    right -= 1 

                #now they both on vowels 
                chars[left], chars[right] = chars[right], chars[left]

                #conitnue 
                left += 1 
                right -= 1

            return "".join(result) 
        """
