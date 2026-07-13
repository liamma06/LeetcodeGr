class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        '''
            -take first word  
            -every word after loop though keep what is repeated 
            -otherwise remove the characters after the first non match 
        '''

        prefix = strs[0]

        for word in strs[1:]: #every word after the first one 
            for i in range(min(len(prefix),len(word))): #take the min 
                if prefix[i] != word[i]: # by default cut at the last since can't go over 
                    prefix = prefix[:i] #slice that point and whatever is after 
                    break
            prefix = prefix[:min(len(prefix),len(word))]

        return prefix 
                
