class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels ={"a","e","i","o","u"} #hashlookup O(1) 
        max_vowel = float('-inf')  
        window_vowel = 0        

        left = 0 
        
        for right in range(len(s)):
            if s[right] in vowels:
                window_vowel += 1 
            
            if (right-left + 1) == k :
                max_vowel = max(window_vowel, max_vowel)

                #early exit 
                if max_vowel == k:
                    return max_vowel

                #slide window
                if s[left] in vowels:
                    window_vowel -= 1 
                left += 1 
            
        return max_vowel

        #O(n) 
