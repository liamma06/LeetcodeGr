class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mapping = {}

        for num in nums:
            mapping[num] = mapping.get(num,0) + 1 
        
        #first intution is to sort it by the value reverse and get loop through and take first K however sorting would be O(nlogn) 

        #bucket sort. 
        buckets = [] 

       # you would need + 1 here because all possible frequency so that mean going from len (6) 0,1,2,3,4,5 possible all 6 is the same so it should go from 0,1,2,3,4,5,6

        for i in range(len(nums) + 1 ): 
            buckets.append([]) # filling it empty
        
         #items ebcasue we iterate without directly changing the dict we just changing like what inside 
        for key,freq in mapping.items():
            buckets[freq].append(key) #3: [1]

        result  = [] 

        #starting from the end add values
        #need the minus one because of index like even though length is 6 we start at 5 as alst term. 
        '''
            buckets = [ [], [], [], [], [], [], [] ]
            # indices:   0   1   2   3   4   5   6
        '''
        for freq in range(len(buckets) - 1,0 , -1):
            for num in buckets[freq]: 
                result.append(num)
                if len(result) == k:
                    return result

        return result 



