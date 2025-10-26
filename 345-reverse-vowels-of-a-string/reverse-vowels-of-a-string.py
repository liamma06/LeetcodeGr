class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = []
        new = []

        for char in s:
            if char in 'aeiouAEIOU':
                vowels.append(char)
            
        for char in s:
            if char in 'aeiouAEIOU':
                new.append(vowels[-1])
                vowels.pop()
            else:
                new.append(char)
            
        return ''.join(new)