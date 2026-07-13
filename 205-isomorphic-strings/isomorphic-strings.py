class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        '''
            hashmap 
            is to check if already inside and if the other character matches and import to check bot h sides could be opposite order 
        '''

        mapping_s_to_t = {} 
        mapping_t_to_s = {}

        #need to check both sides case: ab vs aa would work one way need other check 
        for i in range(len(s)): # O(n) 
            char_s = s[i]
            char_t = t[i]

            if char_s in mapping_s_to_t:
                if mapping_s_to_t[char_s] != char_t: # check if itcurrently matches waht is there 
                    return False
            else:
                mapping_s_to_t[char_s] = char_t 

            if char_t in mapping_t_to_s:
                if mapping_t_to_s[char_t] != char_s:
                    return False
            else:
                mapping_t_to_s[char_t] = char_s
        
        return True 

            

