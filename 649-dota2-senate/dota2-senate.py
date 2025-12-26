from collections import deque
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        

        radiant = deque()
        dire = deque()
        n = len(senate)

        for i in range(len(senate)):
            if senate[i] == "R":
                radiant.append(i)
            elif senate[i] =="D":
                dire.append(i)

        
        while radiant and dire :
            r = radiant[0]
            d = dire[0] 

            if r < d: # radiant first 
                dire.popleft()       # banned
                radiant.popleft()    # used their turn
                radiant.append(r + n)  # move Radiant to next cycle
            else:
                radiant.popleft()
                dire.popleft()
                dire.append(d + n)

        if radiant:
            return "Radiant"
        else:
            return "Dire"
