class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        max_vowel = 0
        curr = 0
        nums_of_shifts = len(s) - k + 1

        if len(s)==1 and s in "aeiou":
            return 1

        for i in range(k):
            if s[i] in "aeiou":
                curr += 1

        max_vowel = max(max_vowel, curr)

        for i in range(1,nums_of_shifts):
            if s[i -1] in "aeiou":
                curr -= 1
            if s[i+k-1] in "aeiou":
                curr += 1
            max_vowel = max(curr,max_vowel)
        
        return max_vowel
        