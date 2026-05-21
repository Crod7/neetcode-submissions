class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hashmap = {"}":"{", "]":"[", ")":"("}

        for c in s:
            if c in hashmap:
                if len(stack) == 0 or hashmap[c] != stack[-1]:
                    return False
                else:
                    stack.pop()
            else:
                stack.append(c)
        
        
        if len(stack) > 0:
            return False
        return True


