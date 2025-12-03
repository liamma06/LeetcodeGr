class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        hashmap = {}

        for num in arr:
            if num in hashmap:
                hashmap[num] += 1 
            else:
                hashmap[num] = 1

        dup = [] 

        for val in hashmap:
            if hashmap[val] in dup:
                return False
            dup.append(hashmap[val])
        return True