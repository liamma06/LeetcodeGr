class Solution:
    def reverseWords(self, s: str) -> str:
        s_trim = s.strip()
        words = s_trim.split() 
        return " ".join(reversed(words))
        