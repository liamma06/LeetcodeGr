class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        result = {} 

        #need to load the inital one 
        for char in words[0]:
            result[char] = result.get(char, 0 ) + 1 

        #we now have freq map or each character 
        #lets check if the other words have the same characters 

        for word in words[1:]:
            current = {} #map for the current word 

            #freq for each char in the current word 
            for char in word:
                current[char] = current.get(char,0) + 1 

            #we want to see if there is a match with the inital mapping to this word frequency mappings 
            for char in list(result): 
                if char in current:
                    result[char] = min(result[char], current[char]) # take the min because what both of them have not just one 
                else:
                    result[char] = 0 

        final = []

        for char, freq in result.items(): #depending on freq we want that many inside the final answer. 
            for i in range(freq):
                final.append(char)

        return final 
            
            
