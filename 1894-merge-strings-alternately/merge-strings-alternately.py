class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        final = [] 
        i = 0 

        while i < len(word1) or i < len(word2):
            if i < len(word1):
                final.append(word1[i])
            if i < len(word2):
                final.append(word2[i])
            i += 1
        return "".join(final)
