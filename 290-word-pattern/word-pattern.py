class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        mapping_c_to_w = {}
        mapping_w_to_c = {}

        words = s.split()

        if len(words) != len(pattern):
            return False 

        for i in range(len(pattern)):
            curr_word = words[i]
            curr_char = pattern[i]

            if curr_char in mapping_c_to_w:
                if mapping_c_to_w[curr_char] != curr_word:
                    return False
            else:
                mapping_c_to_w[curr_char] = curr_word

            if curr_word in mapping_w_to_c:
                if mapping_w_to_c[curr_word] != curr_char:
                    return False
            else:
                mapping_w_to_c[curr_word] = curr_char

        return True 

