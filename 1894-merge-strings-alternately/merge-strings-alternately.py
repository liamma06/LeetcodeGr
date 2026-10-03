class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        least = min(len(word1), len(word2))

        word1_array = list(word1)
        word2_array= list(word2)
        result = []
        final = ""

        for i in range(least):
            result.append(word1_array[i])
            result.append(word2_array[i])

        if len(word1_array) > least:
            final = result + word1_array[least:]
        
        elif len(word2_array) > least:
            final = result + word2_array[least:]
        else:
            final = result
        
        return "".join(final)
