class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        result = []
        target_point = 0#track inside the target

        for i in range(1,n+1):
            if target_point == len(target): #all numbers are found
                break
            
            #always push but pop when needed
            result.append("Push")
            if i == target[target_point]:
                target_point +=1
            else:
                result.append("Pop")

        return result 
