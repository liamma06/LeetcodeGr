class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [] #STORES INDEX
        answer = [0] * (len(temperatures))

        for i in range(len(temperatures)):
            #if something on stack we want to check if it is less than the current temeprature index( warmer )
            while stack and temperatures[i] > temperatures[stack[-1]]:
                # we have a temp warmer so pop off the top
                top_stack_idx = stack.pop()
                days = i - top_stack_idx
                answer[top_stack_idx] = days # add it into the spot where the index was     

            stack.append(i)# add the index of the next temperature 
        
        return answer




        