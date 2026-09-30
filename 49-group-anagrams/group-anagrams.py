class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        store = {} 

        for word in strs:
            sortd = ''.join(sorted(word))

            if sortd not in store:
                store[sortd] = []
                
            store[sortd].append(word) 

        return list(store.values())

