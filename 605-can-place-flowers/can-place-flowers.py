class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        possible = 0 

        if n == 0 :
            return True
        
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0:
                #inital case first 
                if (i == 0 and (len(flowerbed) == 1 or flowerbed[i + 1] == 0 )):
                    possible += 1 
                    flowerbed[i] = 1 
                #last position
                elif (i == len(flowerbed) - 1 ) and flowerbed[i-1] == 0 :
                    possible += 1  
                    flowerbed[i] = 1 
                #somewhere in the middle
                elif flowerbed[i - 1] == 0 and flowerbed[i+1] ==0:
                    possible += 1
                    flowerbed[i] = 1
                
                #check after see if fullfilled
                if possible == n :
                    return True 
                
        return False
        
        #O(n) because it is only 1 loop 
