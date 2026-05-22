class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [(p,s) for p,s in zip(position, speed)]
        stack = []
        print(pair)
        for p,s in sorted(pair)[::-1]:
            value = (target - p) / s
            stack.append(value)
            if len(stack) > 1 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)