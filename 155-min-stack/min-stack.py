class MinStack:

    def __init__(self):
        self.stack = [] 
        self.minStack = [] 
        

    def push(self, value: int) -> None:
        self.stack.append(value)

        #empty
        if not self.minStack:
            self.minStack.append(value)
        #check if less than top of minstack
        elif value < self.minStack[-1] :
            self.minStack.append(value)
        else:
            #same min at this step so append same 
            self.minStack.append(self.minStack[-1])


    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minStack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()