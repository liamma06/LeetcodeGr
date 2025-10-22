class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        result = [] 
        max = candies[0] 
        for i in range(len(candies)):
            if  candies[i] > max:
                max = candies[i]  
            
        for i in range(len(candies)):
            if (candies[i]+extraCandies) >= max:
                result.append(True)
            else:
                result.append(False)
        
        return result