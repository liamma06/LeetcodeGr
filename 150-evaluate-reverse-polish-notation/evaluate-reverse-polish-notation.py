class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        #keep track of numbers and when there an opp take off to do the operation. 

        stack = [] 
        for token in tokens:
            if token in ["+", "-", "*", "/"]:
                b = stack.pop()
                a = stack.pop()
                if token == '+':
                    stack.append(a + b)
                elif token == '-':
                    stack.append(a-b)
                elif token == '*':
                    stack.append(a*b)
                elif token == '/':
                    stack.append(int(a/b))
            else:
                stack.append(int(token))
        return stack[-1]