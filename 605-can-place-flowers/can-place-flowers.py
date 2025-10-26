class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        possible = 0

        if n == 0:
            return True

        for i in range(len(flowerbed)): 
            if flowerbed[i] == 0:
                if i == 0 and (len(flowerbed) == 1 or flowerbed[i+1] == 0):
                    possible += 1
                    flowerbed[i] = 1
                elif i == (len(flowerbed) - 1) and flowerbed[i-1] == 0:
                    possible += 1
                    flowerbed[i] = 1
                elif flowerbed[i-1] == 0 and flowerbed[i+1] == 0:
                    possible += 1
                    flowerbed[i] = 1
                if possible == n:
                    return True



        return False
                
