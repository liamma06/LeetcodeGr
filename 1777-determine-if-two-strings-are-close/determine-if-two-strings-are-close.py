class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False

        # build out freq maps 
        freq_word1 = {}
        freq_word2 = {}

        for i in range(len(word1)): #O(n) 
            if word1[i] in freq_word1: #O(1) lookups 
                freq_word1[word1[i]] += 1 
            elif word1[i] not in freq_word1:
                freq_word1[word1[i]] = 1 

            if word2[i] in freq_word2:
                freq_word2[word2[i]] += 1 
            elif word2[i] not in freq_word2:
                freq_word2[word2[i]] = 1 

        #op 1 tells use order doesn't matter (but need same letters)
        if freq_word1.keys() != freq_word2.keys():
            # set compare 
            return False

        word1_vals = sorted(freq_word1.values()) #O(k log k) const tho 
        word2_vals = sorted(freq_word2.values())

        return word1_vals == word2_vals

        #overall is O(n) 
        