class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        mapping_s = {}
        mapping_t = {} 

        for char in s:
            mapping_s[char] = mapping_s.get(char,0) + 1 

        for char in t:
            mapping_t[char] = mapping_t.get(char,0) + 1 

        if mapping_s == mapping_t:
            return True
        else:
            return False