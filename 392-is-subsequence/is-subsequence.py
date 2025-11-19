class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        ls = 0 

        if len(s) > len(t):
            return False 
        if len(s) == 0:
            return True
        
        
        for char in t:
            if char == s[ls]:
                ls += 1 
                if ls >= len(s):
                    return True
        return False 

