class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        sorted_map = {} 

        for word in strs:
            #sorted returns a list 
            sorted_word = "".join(sorted(word)) # convert back word

            #initalize empty array
            if sorted_word not in sorted_map:
                sorted_map[sorted_word] = []

            #append into sorted section
            sorted_map[sorted_word].append(word)

        return list(sorted_map.values())

        """
            sorting every word O(n * L log L) 
            loop through is O(n)
            the lookup is O(1)

            overall is O(n * L) since the sort is somewhat const with the letter of alpahbet 
        """


