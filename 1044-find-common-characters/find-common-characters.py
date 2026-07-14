class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        result = {} 

        #load in first word as the base case 
        for char in words[0]:
            result[char] = result.get(char, 0 ) + 1 

        '''
            We now need to go through every word after the first one and bascially check if it has similar characters 
            - hashmap of each 
            - check if both have it and take the minimum 
            -otherwise just remove 
        '''

        for word in words[1:]:
            current = {} #hashmap for the current word 

            for char in word:
                current[char] = current.get(char,0) + 1 

            #go through the result mappings 
            for char in list(result):
                if char in current: #if that char is inside current mapping 
                    result[char] = min (current[char],result[char]) # take the least of either
                else:
                    result[char] = 0 # remove bascially

        ans = [] 

        #loop through the final list 
        for key, freq in result.items():
            for i in range(freq): #repeat number of times into the ans 
                ans.append(key)

        return ans

            
        
            
