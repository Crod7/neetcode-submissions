class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        temp = []

        result = []

        for i, t in enumerate(reversed(temperatures)):
            days = 0
            # init case
            if i == 0:
                result.insert(0, 0)
                stack.append(t)
                continue
            print(stack)
            
            # pop stack to find next highest day, count each day
            while stack and t >= stack[-1]:
                value = stack.pop()
                temp.append(value)
                days += 1
            
            if stack and t < stack[-1]:
                days += 1

            if len(stack) == 0:
                days = 0
            # re-add popped days, and append newest day to top
            while temp:
                value = temp.pop()
                stack.append(value)
            stack.append(t)
            # set days till next highest day in result (insert)
            result.insert(0, days)

        return result

                

