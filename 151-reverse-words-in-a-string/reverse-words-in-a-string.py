class Solution:
    def reverseWords(self, s: str) -> str:
        cleaned = s.strip()

        s_list = cleaned.split()
        result = [] 

        for i in range(len(s_list)):
            curr = s_list.pop()
            result.append(curr)

        return " ".join(result)


        #O(n) 