class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = "AEIOUaeiou"
        storage = [] 

        for char in s:
            if char in vowels:
                storage.append(char)
        
        result = []
        for i in range(len(s)):
            if s[i] in vowels:
                result.append(storage.pop())
            else:
                result.append(s[i])
        
        return "".join(result)