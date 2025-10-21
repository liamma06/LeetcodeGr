class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:
            return ""
        
        repeatLength = gcd(len(str1),len(str2))

        repeat=[]
        for i in range(repeatLength):
            repeat.append(str1[i])
        
        return "".join(repeat)