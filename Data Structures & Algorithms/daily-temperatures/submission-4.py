class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        temp = []
        result = []
        
        for i, t in enumerate(reversed(temperatures)):
            #
            days = 0

            if i == 0:
                stack.append(t)
                result.append(0)
                continue
            
            if stack and t >= stack[-1]:
                while stack and t >= stack[-1]:
                    value = stack.pop()
                    temp.append(value)
                
                temp.insert(0, t)
                
            else:
                temp.insert(0, t)
            
            print(t, ": ", temp)
            days = len(temp)
            # no greater temperature found
            if len(stack) <= 0:
                days = 0
            
            result.insert(0, days)

            

            # rebuild stack and empty temp
            while temp:
                value = temp.pop()
                stack.append(value)
        return result
            




