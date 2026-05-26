class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        
        for i,n in enumerate(tokens):
            if n == "+":
                value2 = int(stack.pop())
                value1 = int(stack.pop())
                result = value1 + value2
                stack.append(result)
            elif n == "-":
                value2 = int(stack.pop())
                value1 = int(stack.pop())
                result = value1 - value2
                stack.append(result)
            elif n == "*":
                value2 = int(stack.pop())
                value1 = int(stack.pop())
                result = value1 * value2
                stack.append(result)
            elif n == "/":
                value2 = int(stack.pop())
                value1 = int(stack.pop())
                result = math.trunc(value1 / value2)
                stack.append(result)
            else:
                stack.append(n)
            print(stack)
        return int(stack[0])
            
        
            

            


