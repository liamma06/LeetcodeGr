class Solution:
    def reverseWords(self, s: str) -> str:
        s_clean = s.strip()

        s = s_clean.split() 
        result = [] 

        for i in range(len(s)):
            curr = s.pop()
            result.append(curr)

        return " ".join(result)