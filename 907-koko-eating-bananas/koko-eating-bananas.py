import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #what's the one speed k, applied uniformly to every pile, that lets the sum of all piles' hours fit within h?

        #range of speed 
        left = 1
        right = max(piles) 
        best_rate = 0

        while(left <= right):
            mid = (left + right) // 2

            total_hours_at_rate = 0 

            for pile in piles:
                #round up! 
                hours_for_pile = math.ceil(pile/mid)
                total_hours_at_rate += hours_for_pile
            
            #compare total hours at rate vs the hours allowed
            if total_hours_at_rate <= h :
                # at this rate it alway the LEAST rate so best already
                best_rate = mid

                #at a lower rate does it still perform
                right = mid - 1 
            else:
                #need to increase rate 
                left = mid + 1 

        return best_rate


                
